from django.contrib import admin
from services.models import UsedSms, UsedBanner, BannerPack, SmsPack, CartSms, CartBanner,Order, ReportProduct, ReportShop, Ticket, IPAddress, DailyProductView, DailyShopView

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
