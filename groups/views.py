from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
# Create your views here.

from django.urls import reverse
from django.views import generic
from group.models import Group, GroupMember

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    # Creating a group
    fields = ('name', 'description')
    model = Group


class SingleGroup(generic.DetailView):
    # Viewing a single group
    model = Group

class ListGroups(generic.ListView):
    # List of groups
    model = Group