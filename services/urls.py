from django.urls import path
from services import api

app_name = 'services'

urlpatterns = [
    # SmsPack
    path('sms-pack/create/', api.SmsPackCreate.as_view(), name="sms_pack_create"),
    path('sms-pack/rud/<int:pk>', api.SmsPackRUD.as_view(), name="sms_pack_rud"),
    path('sms-pack/list', api.SmsPackList.as_view(), name="sms_pack_list"),
    # BannerPack
    path('banner-pack/create/', api.BannerPackCreate.as_view()),
    path('banner-pack/rud/<int:pk>', api.BannerPackRUD.as_view()),
    path('banner-pack/list', api.BannerPackList.as_view()),
    # Recommended-Product-Pack
    path('product-pack/create/', api.RecommendedProductPackCreate.as_view()),
    path('product-pack/rud/<int:pk>', api.RecommendedProductPackRUD.as_view()),
    path('product-pack/list', api.RecommendedProductPackList.as_view()),
    # Recommended-Shop-Pack
    path('shop-pack/create/', api.RecommendedShopPackCreate.as_view()),
    path('shop-pack/rud/<int:pk>', api.RecommendedShopPackRUD.as_view()),
    path('shop-pack/list', api.RecommendedShopPackList.as_view()),
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
    # CartBanner
    path('cart-banner/create/', api.CartBannerCreate.as_view()),
    path('cart-banner/rud/<int:pk>', api.CartBannerRUD.as_view()),
    path('cart-banner/list', api.CartBannerList.as_view()),
    # CartSms
    path('cart-sms/create/', api.CartSmsCreate.as_view()),
    path('cart-sms/rud/<int:pk>', api.CartSmsRUD.as_view()),
    path('cart-sms/list', api.CartSmsList.as_view()),
    # CartRecommended-Shop
    path('cart-shop/create/', api.CartRecommendedProductCreate.as_view()),
    path('cart-shop/rud/<int:pk>', api.CartRecommendedProductRUD.as_view()),
    path('cart-shop/list', api.CartRecommendedProductList.as_view()),
    # CartRecommended-Product
    path('cart-product/create/', api.CartSmsCreate.as_view()),
    path('cart-product/rud/<int:pk>', api.CartSmsRUD.as_view()),
    path('cart-product/list', api.CartSmsList.as_view()),
    # Order
    path('order/create/', api.OrderCreate.as_view()),
    path('order/rud/<int:pk>', api.OrderRUD.as_view()),
    path('order/list', api.OrderList.as_view()),
    # UsedBanner
    path('used-banner/create/', api.UsedBannerCreate.as_view()),
    path('used-banner/rud/<int:pk>', api.UsedBannerRUD.as_view()),
    path('used-banner/list', api.UsedBannerList.as_view()),
    # UsedSms
    path('used-sms/create/', api.UsedSmsCreate.as_view()),
    path('used-sms/rud/<int:pk>', api.UsedSmsRUD.as_view()),
    path('used-sms/list', api.UsedSmsList.as_view()),
    # UsedRecommended-Product
    path('used-product/create/', api.UsedRecommendedProductCreate.as_view()),
    path('used-product/rud/<int:pk>', api.UsedRecommendedProductRUD.as_view()),
    path('used-product/list', api.UsedRecommendedProductList.as_view()),
    # UsedRecommended-Shop
    path('used-shop/create/', api.UsedRecommendedShopCreate.as_view()),
    path('used-shop/rud/<int:pk>', api.UsedRecommendedShopRUD.as_view()),
    path('used-shop/list', api.UsedRecommendedShopList.as_view()),

]
