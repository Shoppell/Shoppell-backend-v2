from django.db import models
from services.models import(
    BannerPack, SmsPack,
    RecommendedProductPack, RecommendedShopPack
)
from user_auth.models import User
from shop.models import Product, Shop
from PIL import Image

def resize(nameOfFile):
    img = Image.open(nameOfFile)
    size = (200, int(img.size[1] * 200 / img.size[0]))
    img.resize(size, Image.ANTIALIAS).save(nameOfFile)
    img.save(nameOfFile)
    
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

