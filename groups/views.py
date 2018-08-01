from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db import models
from django.db import IntegrityError
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
# Create your views here.

from django.urls import reverse
from django.views import generic
from groups.models import Group, GroupMember

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    # Creating a group
    fields = ('name', 'description')
    # Connecting to the model
    model = Group


class SingleGroup(generic.DetailView):
    # Viewing a single group
    model = Group

class ListGroups(generic.ListView):
    # List of groups
    model = Group

class JoinGroup(LoginRequiredMixin, generic.RedirectView):
    # Joining a group

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    # Checks in case user is in group
    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))
        
        # Checking if user can perform specifc actions
        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request,'Warning, you are already a member!')
        else:
            messages.success(self.request, 'You are now successfully a member!')
        return super().get(request,*args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):
    # Leaving a group
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    # Checking if user is in the group in order to leave
    def get(self, request, *args, **kwargs):
         
        try:
            membership = GroupMember.objects.filter(user=self.request.user,group__slug=self.kwargs.get('slug')).get()
        except GroupMember.DoesNotExist:
            messages.warning(self.request, 'Sorry, you are not in this group!')
        else:
            membership.delete()
            messages.success(self.request, 'You have successfully left the group!')
        return super().get(request, *args, **kwargs)


