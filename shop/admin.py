from django.contrib import admin
from .models import Product, Shop, Category, ShopComment, ProductComment, SavedProduct, FavoriteShop, SocialMedia, SocialMediaLink, Evidence

admin.site.register(SocialMedia)
admin.site.register(SocialMediaLink)
admin.site.register(Evidence)
admin.site.register(Category)
admin.site.register(ShopComment)
admin.site.register(ProductComment)
admin.site.register(SavedProduct)
admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(FavoriteShop)
