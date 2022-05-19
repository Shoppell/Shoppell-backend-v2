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
    


]
