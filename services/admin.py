from django.contrib import admin
from services.models import(
UsedSms, UsedBanner, BannerPack, SmsPack, CartSms,
 CartBanner,Order, ReportProduct, ReportShop, Ticket,
  IPAddress, DailyProductView, DailyShopView, RecommendedProductPack,
 RecommendedShopPack, CartRecommendedShop, CartRecommendedProduct,
  UsedRecommendedProduct, UsedRecommendedShop, CustomSms
) 

admin.site.register(CustomSms)
admin.site.register(RecommendedProductPack)
admin.site.register(RecommendedShopPack)
admin.site.register(CartRecommendedProduct)
admin.site.register(CartRecommendedShop)
admin.site.register(UsedRecommendedProduct)
admin.site.register(UsedRecommendedShop)
admin.site.register(IPAddress)
admin.site.register(DailyProductView)
admin.site.register(DailyShopView)
admin.site.register(UsedBanner)
admin.site.register(UsedSms)
admin.site.register(BannerPack)
admin.site.register(SmsPack)
admin.site.register(CartSms)
admin.site.register(CartBanner)
admin.site.register(Order)
admin.site.register(ReportProduct)
admin.site.register(ReportShop)
admin.site.register(Ticket)
