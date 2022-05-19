from django.contrib import admin
from services.models import(
 BannerPack, SmsPack, RecommendedProductPack,
 RecommendedShopPack, CustomSms
) 

admin.site.register(CustomSms)
admin.site.register(RecommendedProductPack)
admin.site.register(RecommendedShopPack)
admin.site.register(BannerPack)
admin.site.register(SmsPack)
