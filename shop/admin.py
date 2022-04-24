from django.contrib import admin
from .models import Product, Shop, Category, ProductImage

admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Product)
