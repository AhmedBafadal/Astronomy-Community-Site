from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from djano.views import generic
from django.http import Http404
from braces.views import SelectRelatedMixin

from . import models
from . import forms

from django.contrib.auth import get_user_model
# Allowing calls to the user model
User = get_user_model()

class PostList(SelectRelatedMixin, generic.ListView):
    # List of posts belonging to a group
    model = models.Post # Connecting to the Post model
    select_related = ('user', 'group') # Provides a tuple of related models (e.g. Foreign Keys)

class UserPosts(generic.ListView):
    model = models.Post 
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            # Fetching posts related to a username
            self.post.user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))

        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context
    
class PostDetail(SelectRelatedMixin, generic.DetailView):
    # DetailView when clicking on a post

    model = models.Post 
    select_related = ('user', 'group') 

    def get_queryset(self):
        # Ensuring username is correct
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('message', 'group')
    model = models.Post

    def form_valid(self, form):
        # Connecting the post to the user
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    # Deleting a post
    
    model = models.Post
    select_related = ('user','group')
    succes_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Post Deleted')
        return super().delete(*args, **kwargs)


    