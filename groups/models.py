# from django.db import models
# from django.utils.text import slugify
# # Create your models here.
# from django.urls import reverse
# import misaka

# # Returning the user model that's currently active
# from django.contrib.auth import get_user_model
# # Allows calls from current user's session
# User = get_user_model()

# # Custom template tags
# from django import template
# register = template.Library()


# class Group(models.Model):
#     # Name of the group (must be unique)
#     name = models.CharField(max_length=255, unique=True)
#     # Preventing error in calling url codes
#     slug = models.SlugField(allow_unicode=True, unique=True)
#     # Description field
#     description = models.TextField(blank=True, default='')
#     description_html = models.TextField(editable=False, default='', blank=True)
#     # Members of the group
#     members = models.ManyToManyField(User, through='GroupMember')

#     def __str__(self):
#         return self.name

#     # Saving the group
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         self.description_html = misaka.html(self.description)
#         super().save(*args, **kwargs)

#     def get_absolute_url(self):
#         return reverse('groups:single', kwargs={'slug': self.slug})

#     class Meta:
#         # Order by name
#         ordering = ['name']


# class GroupMember(models.Model):
#     # Each group member is related to the group class
#     group = models.ForeignKey(Group, related_name='memberships',on_delete=models.CASCADE)

#     # Linking users with the various groups they belong to
#     user = models.ForeignKey(User, related_name='user_groups',on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username

#     class Meta:
#         # Linking groups and users
#         unqiue_together = ('group', 'user')

###
import misaka
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
# from accounts.models import User

from django.contrib.auth import get_user_model
User = get_user_model()

# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag
from django import template
register = template.Library()



class Group(models.Model):
    # Group name
    name = models.CharField(max_length=255, unique=True)
    # Group slug
    slug = models.SlugField(allow_unicode=True, unique=True)
    # Group description
    description = models.TextField(blank=True, default='')
    # Group markdown description
    description_html = models.TextField(editable=False, default='', blank=True)
    # Group members
    members = models.ManyToManyField(User,through="GroupMember")

    def __str__(self):
        return self.name
    
    # Save group
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})


    class Meta:
        # Ordered by name
        ordering = ["name"]


class GroupMember(models.Model):
    # Group user belongs to
    group = models.ForeignKey(Group, related_name="memberships",on_delete=models.CASCADE)
    # User
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
         # Linking every group to a user
        unique_together = ("group", "user")
