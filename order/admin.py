from django.contrib import admin
from order.models import(
    Order, UsedRecommendedProduct, 
    UsedBanner, UsedRecommendedShop,
    UsedSms
)
admin.site.register(Order)
admin.site.register(UsedBanner)
admin.site.register(UsedRecommendedProduct)
admin.site.register(UsedRecommendedShop)
admin.site.register(UsedSms)
