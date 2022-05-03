from statistics import mode
from traceback import print_tb
from django.db import models
from django.forms import ImageField
from django.utils import timezone
from user_auth.models import User
from PIL import Image
from persian_tools import digits, separator
from shop.PersianSwear import PersianSwear

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


class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shops')
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
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=1)
    is_ban = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        for x in [self.image, ]:
            if x:
                super().save(*args, **kwargs)
                resize(x.path)
        self.instagram_link = "https://www.instagram.com/"+ self.instagram_link+"/"
        self.whatsapp_link = "https://wa.me/" + self.whatsapp_link 
        self.telegram_link = "https://t.me/" + self.telegram_link
        super().save(*args, **kwargs)

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
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image1 = models.ImageField(upload_to='products')
    image2 = models.ImageField(upload_to='products', blank=True, null=True)
    image3 = models.ImageField(upload_to='products', blank=True, null=True)
    image4 = models.ImageField(upload_to='products', blank=True, null=True)
    image5 = models.ImageField(upload_to='products', blank=True, null=True)
    image6 = models.ImageField(upload_to='products', blank=True, null=True)
    payment_link = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    last_price = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    first_page = models.BooleanField(default=True)
    priority = models.PositiveIntegerField(default=0)
    is_hide = models.PositiveIntegerField(default=False)
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=1)


    def save(self, *args, **kwargs):
        for x in [self.image1, self.image2, self.image3, self.image4, self.image5, self.image6 ]:
            if x:
                super().save(*args, **kwargs)
                resize(x.path)

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
    is_bad = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name +" "+ self.user.mobile

    def save(self, *args, **kwargs):
        persianswear = PersianSwear()
        if persianswear.is_bad(self.description):
            self.is_bad = True
        else:
            self.is_bad = False
        super().save(*args, **kwargs)

class ShopComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    description = models.TextField()
    grade = models.PositiveIntegerField(choices=choices_rate)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.shop.name +" "+ self.user.mobile
    
    def save(self, *args, **kwargs):
        persianswear = PersianSwear()
        if persianswear.is_bad(self.description):
            self.is_bad = True
        else:
            self.is_bad = False
        super().save(*args, **kwargs)

