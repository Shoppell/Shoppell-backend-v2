from django.contrib import admin
from util.models import (
    IPAddress, DailyProductView, DailyShopView, 
    ReportProduct, ReportShop, Ticket
)

admin.site.register(IPAddress)
admin.site.register(DailyProductView)
admin.site.register(DailyShopView)
admin.site.register(ReportProduct)
admin.site.register(ReportShop)
admin.site.register(Ticket)
