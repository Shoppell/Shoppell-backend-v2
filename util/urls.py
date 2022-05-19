from django.urls import path
from util import api

app_name = 'services'

urlpatterns = [
    # ReportProduct
    path('report-product/create/', api.ReportProductCreate.as_view()),
    path('report-product/rud/<int:pk>', api.ReportProductRUD.as_view()),
    path('report-product/list', api.ReportProductList.as_view()),
    # ReportShop
    path('report-shop/create/', api.ReportShopCreate.as_view()),
    path('report-shop/rud/<int:pk>', api.ReportShopRUD.as_view()),
    path('report-shop/list', api.ReportShopList.as_view()),
    # Ticket
    path('ticket/create/', api.TicketCreate.as_view()),
    path('ticket/rud/<int:pk>', api.TicketRUD.as_view()),
    path('ticket/list', api.TicketList.as_view()),
    # IPAddress
    path('ipaddress/create/', api.IPAddressCreate.as_view()),
    path('ipaddress/rud/<int:pk>', api.IPAddressRUD.as_view()),
    path('ipaddress/list', api.IPAddressList.as_view()),
    # DailyProductView
    path('daily-productview/create/', api.DailyProductViewCreate.as_view()),
    path('daily-productview/rud/<int:pk>', api.DailyProductViewRUD.as_view()),
    path('daily-productview/list', api.DailyProductViewList.as_view()),
    # DailyShopView
    path('daily-shopview/create/', api.DailyShopViewCreate.as_view()),
    path('daily-shopview/rud/<int:pk>', api.DailyShopViewRUD.as_view()),
    path('daily-shopview/list', api.DailyShopViewList.as_view()),
]
