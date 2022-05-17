from django.urls import path
from shop import api

app_name = 'shop'

urlpatterns = [
   # product
    path('product/create/', api.ProductCreate.as_view()),
    path('product/rud/<int:pk>', api.ProductRUD.as_view()),
    path('product/list', api.ProductList.as_view()),
    path('product/search', api.ProductSearch.as_view()),
    # shop
    path('shop/create/', api.ShopCreate.as_view()),
    path('shop/rud/<int:pk>', api.ShopRUD.as_view()),
    path('shop/productlist/<int:pk>', api.ShopProductList.as_view()),
    path('shop/list', api.ShopList.as_view()),
    path('shop/search', api.ShopSearch.as_view()),
    # category
    path('category/create/', api.CategoryCreate.as_view()),
    path('category/rud/<int:pk>', api.CategoryRUD.as_view()),
    path('category/list', api.CategoryList.as_view()),
    # saved-product
    path('saved-product/create/', api.SavedProductCreate.as_view()),
    path('saved-product/rud/<int:pk>', api.SavedProductRUD.as_view()),
    path('saved-product/list', api.SavedProductList.as_view()),
    # comment-shop
    path('comment-shop/create/', api.ShopCommentCreate.as_view()),
    path('comment-shop/rud/<int:pk>', api.ShopCommentRUD.as_view()),
    path('comment-shop/list', api.ShopCommentList.as_view()),
    # comment-product
    path('comment-product/create/', api.ProductCommentCreate.as_view()),
    path('comment-product/rud/<int:pk>', api.ProductCommentRUD.as_view()),
    path('comment-product/list', api.ProductCommentList.as_view()),
    
]