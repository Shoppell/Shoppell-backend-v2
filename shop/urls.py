from django.urls import URLPattern, path
from shop import api

urlpatterns = [
    path('product/create/', api.ProductCreate.as_view()),
    path('product/rud/<int:pk>', api.ProductRUD.as_view()),
    path('product/list', api.ProductList.as_view()),
    path('productimage/create/', api.ProductImageCreate.as_view()),
    path('productimage/rud/<int:pk>', api.ProductImageRUD.as_view()),
    path('productimage/list', api.ProductImageList.as_view()),
    path('shop/create/', api.ShopCreate.as_view()),
    path('shop/rud/<int:pk>', api.ShopRUD.as_view()),
    path('shop/list', api.ShopList.as_view()),
    path('category/create/', api.CategoryCreate.as_view()),
    path('category/rud/<int:pk>', api.CategoryRUD.as_view()),
    path('category/list', api.CategoryList.as_view()),

]