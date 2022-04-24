from email.policy import default
from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from user_auth.models import User
from PIL import Image
from persian_tools import digits, separator


def resize(nameOfFile):
    img = Image.open(nameOfFile)
    size = (200, int(img.size[1] * 200 / img.size[0]))
    img.resize(size, Image.ANTIALIAS).save(nameOfFile)
    img.save(nameOfFile)


class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shops')
    cover = models.ImageField(upload_to='cover')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='products_category')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        for x in [self.image, ]:
            if x:
                super().save(*args, **kwargs)
                resize(x.path)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image = models.ImageField(upload_to='products')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        for x in [self.image, ]:
            if x:
                super().save(*args, **kwargs)
                resize(x.path)
    

class Product(models.Model):
    product_images = models.ManyToManyField(ProductImage)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    payment_link = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    last_price = models.PositiveIntegerField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    first_page = models.BooleanField(default=True)
   
    def get_off(self):
        return int(100*(self.last_price/self.price))

    def __str__(self):
        return self.name

