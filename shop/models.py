from statistics import mode
from django.db import models
from django.forms import ImageField
from django.utils import timezone
from user_auth.models import User
from PIL import Image
from persian_tools import digits, separator

choices_rate = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

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
    to_users = models.ManyToManyField(User, related_name="followers")
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

    def __str__(self):
        return self.user.mobile + " " + self.created

class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shops')
    cover = models.ImageField(upload_to='cover', default='media\cover\default_cover.jpg')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=False)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    is_verify = models.BooleanField(default=False)
    priority = models.PositiveIntegerField(default=0)
    instagram_link = models.CharField(max_length=100, blank=True, null=True)
    telegram_link = models.CharField(max_length=100, blank=True, null=True)
    website_link = models.CharField(max_length=100, blank=True, null=True)
    whatsapp_link = models.CharField(max_length=100, blank=True, null=True)
    evidence = models.ImageField(upload_to='evidences', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='products_category')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        for x in [self.image, ]:
            if x:
                super().save(*args, **kwargs)
                resize(x.path)

    def __str__(self):
        return self.name

class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='products')
    image2 = models.ImageField(upload_to='products', blank=True, null=True)
    image3 = models.ImageField(upload_to='products', blank=True, null=True)
    image4 = models.ImageField(upload_to='products', blank=True, null=True)
    image5 = models.ImageField(upload_to='products', blank=True, null=True)
    image6 = models.ImageField(upload_to='products', blank=True, null=True)
    payment_link = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    last_price = models.PositiveIntegerField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    first_page = models.BooleanField(default=True)
    priority = models.PositiveIntegerField(default=0)
   
    def get_off(self):
        return int(100*(self.last_price/self.price))

    def __str__(self):
        return self.name

class SavedProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.product.name +" "+ self.user.mobile

class ProductComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField()
    grade = models.PositiveIntegerField(choices=choices_rate)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.product.name +" "+ self.user.mobile

class ShopComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    description = models.TextField()
    grade = models.PositiveIntegerField(choices=choices_rate)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.shop.name +" "+ self.user.mobile