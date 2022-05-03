from django.db import models
from user_auth.models import User
from shop.models import Shop, Product
from PIL import Image

def resize(nameOfFile):
    img = Image.open(nameOfFile)
    size = (200, int(img.size[1] * 200 / img.size[0]))
    img.resize(size, Image.ANTIALIAS).save(nameOfFile)
    img.save(nameOfFile)

class SmsOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user_mobile = models.CharField(max_length=20)
    text = models.TextField()
    price = models.PositiveIntegerField(default=0)
    to_users = models.JSONField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.user.mobile + " " + self.created

class BannerAd(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shops')
    link = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        for x in [self.image, ]:
            if x:
                super().save(*args, **kwargs)
                resize(x.path)

    def __str__(self):
        return self.user.mobile + " " + self.created

class ReportShop(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.shop.name +" "+ self.user.mobile + " "+ self.title

class ReportProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.product.name +" "+ self.user.mobile+ " "+ self.title

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title +" "+ self.user.mobile

