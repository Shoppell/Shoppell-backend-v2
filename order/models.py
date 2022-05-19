from django.db import models
from user_auth.models import User
from cart.models import CartBanner, CartSms, CartRecommendedShop, CartRecommendedProduct
from shop.models import Product, Shop
from PIL import Image

def resize(nameOfFile):
    img = Image.open(nameOfFile)
    size = (200, int(img.size[1] * 200 / img.size[0]))
    img.resize(size, Image.ANTIALIAS).save(nameOfFile)
    img.save(nameOfFile)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sms_packs = models.ManyToManyField(CartSms, blank=True)
    banner_packs = models.ManyToManyField(CartBanner, blank=True)
    recommended_shop_pack = models.ManyToManyField(CartRecommendedShop, blank=True)
    recommended_product_pack = models.ManyToManyField(CartRecommendedProduct, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.mobile 

class UsedSms(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="user_used_sms")
    user_mobile = models.CharField(max_length=20, blank=True, null=True)
    text = models.TextField()
    to_users = models.ManyToManyField(User, related_name="sms_receiver")
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    counts = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.user_mobile = self.user.mobile
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.mobile 

class UsedBanner(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user_mobile = models.CharField(max_length=20, blank=True, null=True)
    text = models.TextField()
    duration = models.DurationField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    image = models.ImageField(upload_to='banner')

    def save(self, *args, **kwargs):
        for x in [self.image, ]:
            if x:
                super().save(*args, **kwargs)
                resize(x.path)
        self.user_mobile = self.user.mobile
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.mobile 
class UsedRecommendedProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user_mobile = models.CharField(max_length=20, blank=True, null=True)
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    priority = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    image = models.ImageField(upload_to='banner')

    def save(self, *args, **kwargs):
        for x in [self.image, ]:
            if x:
                super().save(*args, **kwargs)
                resize(x.path)
        self.user_mobile = self.user.mobile
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.mobile 

class UsedRecommendedShop(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user_mobile = models.CharField(max_length=20, blank=True, null=True)
    text = models.TextField()
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    priority = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    image = models.ImageField(upload_to='banner')

    def save(self, *args, **kwargs):
        for x in [self.image, ]:
            if x:
                super().save(*args, **kwargs)
                resize(x.path)
        self.user_mobile = self.user.mobile
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.mobile 
