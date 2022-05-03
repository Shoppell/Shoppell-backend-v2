from django.contrib import admin
from services.models import SmsOrder, BannerAd, ReportProduct, ReportShop, Ticket

admin.site.register(SmsOrder)
admin.site.register(BannerAd)
admin.site.register(ReportProduct)
admin.site.register(ReportShop)
admin.site.register(Ticket)
