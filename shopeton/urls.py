from django.contrib import admin
from django.urls import path, include
from user_auth.api import RegisterApi, LoginApi
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from shopeton import settings
from shop import api

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/product/create/', api.ProductCreate.as_view()),
    path('api/v1/product/rud/<int:pk>', api.ProductRUD.as_view()),
    path('api/v1/product/list', api.ProductList.as_view()),
    path('api/v1/shop/create/', api.ShopCreate.as_view()),
    path('api/v1/shop/rud/<int:pk>', api.ShopRUD.as_view()),
    path('api/v1/shop/list', api.ShopList.as_view()),
    path('api/v1/category/create/', api.CategoryCreate.as_view()),
    path('api/v1/category/rud/<int:pk>', api.CategoryRUD.as_view()),
    path('api/v1/category/list', api.CategoryList.as_view()),

    path('api/v1/user/', include('user_auth.urls')),
  
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)