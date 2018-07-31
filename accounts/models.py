from django.db import models
from django.contrib import auth
from django.utils import timezone

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    """
    User Model
    """
    def __str__(self):
        return "@{}".format(self.username)
    