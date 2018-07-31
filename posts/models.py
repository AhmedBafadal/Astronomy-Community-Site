from django.db import models
from django.urls import reverse
from django.conf import settings
import misaka

from groups.models import Group
# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    # User publishing post
    user = models.ForeignKey(User, related_name='posts',on_delete=models.CASCADE)
    # Date of creation of post
    created_at = models.DateTimeField(auto_now=True)
    # Message in the post
    message = models.TextField()
    # HTML markdown message
    message_html = models.TextField(editable = False)
    # Connect posts with groups
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.message

    # Saving posts
    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username, 'pk':self.pk})

    
    class Meta:
        # Descending order for most recent posts
        ordering = ['-created_at']
        # Linking every message to a user
        unique_together = ['user', 'message']
