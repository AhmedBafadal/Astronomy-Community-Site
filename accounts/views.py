from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView



class SignUp(CreateView):
    """
    Sign Up View: Creating a new user
    """
    form_class = forms.UserCreateForm 
    # Upon successful signup, reverse user back to login page
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

