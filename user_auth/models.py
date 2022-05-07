from django.db import models
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
from user_auth.myusermanager import MyUserManager

class User(AbstractUser):
    username = None
    phone = models.CharField(max_length=11, unique=True)
    verifyCode = models.PositiveIntegerField(blank=True, null=True)
    verifyCode_create_time = models.DateTimeField(auto_now=True, null=True)
    instagram_account = models.CharField(max_length=200, blank=True, null=True)
    instagram_verify = models.BooleanField(default=False)
    is_ban = models.BooleanField(default=False)
    is_shop_admin = models.BooleanField(default=False)
    is_shop_owner = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    objects = MyUserManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    backend = 'user_auth.mybackend.MobileBackend'

