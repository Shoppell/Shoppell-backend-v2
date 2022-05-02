from django.contrib import admin
from .models import Product, Shop, Category, ShopComment, ProductComment, SavedProduct, SmsOrder, BannerAd

admin.site.register(Category)
admin.site.register(ShopComment)
admin.site.register(ProductComment)
admin.site.register(SavedProduct)
admin.site.register(SmsOrder)
admin.site.register(Shop)
admin.site.register(Product)
