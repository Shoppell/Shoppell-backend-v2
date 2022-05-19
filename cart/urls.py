from django.urls import path
from cart import api

app_name = 'cart'

urlpatterns = [
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
]
