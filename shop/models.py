from statistics import mode
from traceback import print_tb
from django.db import models
from django.forms import ImageField
from django.utils import timezone
from user_auth.models import User
from PIL import Image
from persian_tools import digits, separator
from shop.PersianSwear import PersianSwear
import uuid
import pytz
import datetime

def time_seprator():
    tz = pytz.timezone('Asia/Tehran')
    datem = datetime.datetime.strptime(tz, "%Y-%m-%d %H:%M:%S")
    print(datem.day)        # 25
    print(datem.month)      # 5
    print(datem.year) 
    return datem

choices_rate = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

choices_evidence = (
   ('instagram-owner', 'instagram-owner'),
   ('valid-pay', 'valid-pay'),
)


def resize(nameOfFile):
    img = Image.open(nameOfFile)
    size = (200, int(img.size[1] * 200 / img.size[0]))
    img.resize(size, Image.ANTIALIAS).save(nameOfFile)
    img.save(nameOfFile)

class Shop(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="owner", blank=True, null=True)
    admins = models.ManyToManyField(User, blank=True, related_name="admins")
    image = models.ImageField(upload_to='shops', default='default/shop.jpg', null=True)
    cover = models.ImageField(upload_to='cover', default='default/cover.jpg', null=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    is_verify = models.BooleanField(default=False)
    priority = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=1)
    is_ban = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        for x in [self.image, self.cover]:
            if x:
                resize(x.path)           
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class SocialMedia(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class SocialMediaLink(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    social_media = models.ForeignKey(SocialMedia, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    link = models.TextField()
    hits = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class Evidence(models.Model):
    type = models.CharField(choices=choices_evidence, max_length=100)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    file = models.FileField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='products_category', default='default/category.png', null=True)
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
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, related_name="shopproduct")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='products', default='default/product.jpg', null=True)
    image2 = models.ImageField(upload_to='products', blank=True, null=True)
    image3 = models.ImageField(upload_to='products', blank=True, null=True)
    image4 = models.ImageField(upload_to='products', blank=True, null=True)
    image5 = models.ImageField(upload_to='products', blank=True, null=True)
    image6 = models.ImageField(upload_to='products', blank=True, null=True)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    last_price = models.PositiveIntegerField()
    off = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    first_page = models.BooleanField(default=True)
    priority = models.PositiveIntegerField(default=0)
    is_hide = models.BooleanField(default=False)
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=1)

    def save(self, *args, **kwargs):
        for x in [self.image1, self.image2, self.image3, self.image4, self.image5, self.image6 ]:
            if x:
                resize(x.path)
        self.off = 100-int(100*(self.last_price/self.price))
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name

class SavedProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.product.name +" "+ self.user.phone

class ProductComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField()
    grade = models.PositiveIntegerField(choices=choices_rate)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_bad = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name +" "+ self.user.phone

    def save(self, *args, **kwargs):
        persianswear = PersianSwear()
        if persianswear.is_bad(self.description):
            self.is_bad = True
        else:
            self.is_bad = False
        num_comments = len(ProductComment.objects.filter(shop=self.product))
        final_rating = (num_comments*self.product.rating + self.grade)/(num_comments+1)
        self.product.rating = final_rating
        self.product.save()
        super().save(*args, **kwargs)

class ShopComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    description = models.TextField()
    grade = models.PositiveIntegerField(choices=choices_rate)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.shop.name +" "+ self.user.phone
    
    def save(self, *args, **kwargs):
        persianswear = PersianSwear()
        if persianswear.is_bad(self.description):
            self.is_bad = True
        else:
            self.is_bad = False
        num_comments = len(ShopComment.objects.filter(shop=self.shop))
        final_rating = (num_comments*self.shop.rating + self.grade)/(num_comments+1)
        self.shop.rating = final_rating
        self.shop.save()
        super().save(*args, **kwargs)

class FavoriteShop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.shop.name +" "+ self.user.phone
