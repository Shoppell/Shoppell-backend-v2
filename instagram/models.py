from django.db import models
from user_auth.models import User


class InstagramAccountClone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instagram_account = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class InstagramPostClone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

