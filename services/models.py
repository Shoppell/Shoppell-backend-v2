from ipaddress import ip_address
# from pyexpat import model
from turtle import mode
from django.db import models
from django.forms import model_to_dict
from user_auth.models import User
from shop.models import Shop, Product
from PIL import Image

def resize(nameOfFile):
    img = Image.open(nameOfFile)
    size = (200, int(img.size[1] * 200 / img.size[0]))
    img.resize(size, Image.ANTIALIAS).save(nameOfFile)
    img.save(nameOfFile)

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
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title +" "+ self.user.mobile

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.ip_address

class DailyProductView(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    view = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.product.name

class DailyShopView(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    view = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.shop.name

#   ip_address = request.user.ip_address
#     if ip_address not in shop.hits.all():
#         shop.hits.add(ip_address)

class CartBanner(models.Model):
    banner_pack = models.ForeignKey(BannerPack, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.user.mobile 
class CartSms(models.Model):
    sms_pack = models.ForeignKey(SmsPack, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.user.mobile 

class CartRecommendedProduct(models.Model):
    recommended_product_pack = models.ForeignKey(RecommendedProductPack, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.user.mobile 

class CartRecommendedShop(models.Model):
    recommended_shop_pack = models.ForeignKey(RecommendedShopPack, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.user.mobile 

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
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
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