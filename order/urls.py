from django.urls import path
from order import api

app_name = 'order'

urlpatterns = [
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
