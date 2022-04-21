from django.contrib import admin
from django.urls import path
from user_auth.api import RegisterApi, LoginApi
from shop import api

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register', RegisterApi.as_view()),
    path('api/verify', LoginApi.as_view()),
    path('api/product/create', api.ProductCreate.as_view()),
    path('api/product/rud', api.ProductRUD.as_view()),
    path('api/product/list', api.ProductList.as_view()),
    path('api/shop/create', api.ShopCreate.as_view()),
    path('api/shop/rud', api.ShopRUD.as_view()),
    path('api/shop/list', api.ShopList.as_view()),
    path('api/category/create', api.CategoryCreate.as_view()),
    path('api/category/rud', api.CategoryRUD.as_view()),
    path('api/category/list', api.CategoryList.as_view()),
   
]