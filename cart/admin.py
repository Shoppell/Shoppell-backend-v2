from django.contrib import admin
from cart.models import(
    CartBanner, CartSms,
    CartRecommendedShop, CartRecommendedProduct
)
admin.site.register(CartBanner)
admin.site.register(CartSms)
admin.site.register(CartRecommendedShop)
admin.site.register(CartRecommendedProduct)
