from django.contrib import admin
from django.urls import path, include
from user_auth.api import RegisterApi, LoginApi
from shop import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('shop.urls')),
    path('api/v1/user/', include('user_auth.urls')),
  
]