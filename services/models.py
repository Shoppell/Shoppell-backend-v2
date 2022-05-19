from ipaddress import ip_address
# from pyexpat import model
from turtle import mode
from django.db import models
from django.forms import model_to_dict
from user_auth.models import User
from shop.models import Shop, Product
from PIL import Image
from .sms import send_custom_text

def resize(nameOfFile):
    img = Image.open(nameOfFile)
    size = (200, int(img.size[1] * 200 / img.size[0]))
    img.resize(size, Image.ANTIALIAS).save(nameOfFile)
    img.save(nameOfFile)

class CustomSms(models.Model):
    phone = models.CharField(max_length=11, blank=False, null=True)
    text = models.TextField(blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        send_custom_text(self.phone, self.text)

    def __str__(self):
        return self.text[0:10]

class SmsPack(models.Model):
    image = models.ImageField(upload_to='sms-pack')
    count = models.IntegerField(default=0)
    price = models.IntegerField()
    last_price = models.IntegerField()
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        for x in [self.image, ]:
            if x:
                super().save(*args, **kwargs)
                resize(x.path)

    def __str__(self):
        return self.title
        
class BannerPack(models.Model):
    image = models.ImageField(upload_to='banner-pack')
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    price = models.IntegerField()
    last_price = models.IntegerField()
    duration = models.DurationField()

    def save(self, *args, **kwargs):
        for x in [self.image, ]:
            if x:
                super().save(*args, **kwargs)
                resize(x.path)

    def __str__(self):
        return self.title

class RecommendedProductPack(models.Model):
    image = models.ImageField(upload_to='recommended-product-pack')
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    price = models.IntegerField()
    last_price = models.IntegerField()
    priority = models.IntegerField()

    def save(self, *args, **kwargs):
        for x in [self.image, ]:
            if x:
                super().save(*args, **kwargs)
                resize(x.path)

    def __str__(self):
        return self.title

class RecommendedShopPack(models.Model):
    image = models.ImageField(upload_to='recommended-shop-pack')
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    price = models.IntegerField()
    last_price = models.IntegerField()
    priority = models.IntegerField()

    def save(self, *args, **kwargs):
        for x in [self.image, ]:
            if x:
                super().save(*args, **kwargs)
                resize(x.path)

    def __str__(self):
        return self.title
