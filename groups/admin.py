from django.contrib import admin
from . import models
# Register your models here.
# Using tabular inline class allows utilisation of admin interface with the ability to edit models on the same page as the parent model
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)