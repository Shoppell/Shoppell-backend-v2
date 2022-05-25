from django.urls import path
from shop import api

app_name = 'shop'

urlpatterns = [
    # product
    path('product/create/', api.ProductCreate.as_view(), name="product_create"),
    path('product/read/<int:pk>', api.ProductRead.as_view()),
    path('product/rud/<int:pk>', api.ProductRUD.as_view()),
    path('product/list', api.ProductList.as_view()),
    path('product/search', api.ProductSearch.as_view()),
    # shop
    path('shop/create/', api.ShopCreate.as_view(), name="shop_create"),
    path('shop/read/<slug:slug>', api.ShopRead.as_view(), name="shop_rud"),
    path('shop/rud/<slug:slug>', api.ShopRUD.as_view(), name="shop_rud"),
    path('shop/productlist/<slug:slug>', api.ShopProductListUser.as_view(), name="shop_product_list_user"),
    path('shop/productlist', api.ShopProductList.as_view(), name="shop_product_list"),
    path('shop/list', api.ShopList.as_view(), name="shop_list"),
    path('shop/search', api.ShopSearch.as_view(), name="shop_search"),
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
    path('comment-shop/list/<int:pk>', api.ShopCommentList.as_view()),
    # comment-product
    path('comment-product/create/', api.ProductCommentCreate.as_view()),
    path('comment-product/rud/<int:pk>', api.ProductCommentRUD.as_view()),
    path('comment-product/list/<int:pk>', api.ProductCommentList.as_view()),
    
]