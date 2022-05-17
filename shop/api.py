from email.policy import HTTP
from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from .serializer import(
ShopSerializer, ProductSerializer, CategorySerializer,
 ProductSearchSeralizer, ShopSearchSeralizer, SavedProductSerializer,
  ShopCommentSerializer, ProductCommentSerializer,
  ProductShowSerializer
) 
from user_auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Product, Shop, Category, SavedProduct, ShopComment, ProductComment
from django.contrib.postgres.search import TrigramSimilarity
from rest_framework.views import APIView
from django.db.models import Avg, Max, Min
import random

class SavedProductCreate(generics.GenericAPIView):
 
    def post(self, request, *args, **kwargs):
        serializer = SavedProductSerializer(data=request.data)
        print(serializer.initial_data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user=request.user)
        return Response(SavedProductSerializer(new_serializer).data)

class SavedProductList(generics.ListAPIView):
    queryset = SavedProduct.objects.all()
    serializer_class = SavedProductSerializer

class SavedProductRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = SavedProduct.objects.all()
    serializer_class = SavedProductSerializer

class ShopCommentCreate(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        serializer = ShopCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user=request.user)
        return Response(ShopCommentSerializer(new_serializer).data)

class ShopCommentList(generics.ListAPIView):
    queryset = ShopComment.objects.all()
    serializer_class = ShopCommentSerializer

class ShopCommentRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShopComment.objects.all()
    serializer_class = ShopCommentSerializer

class ProductCommentCreate(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = ProductCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user=request.user)
        return Response(ProductCommentSerializer(new_serializer).data)

class ProductCommentList(generics.ListAPIView):
    queryset = ProductComment.objects.all()
    serializer_class = ProductCommentSerializer

class ProductCommentRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductComment.objects.all()
    serializer_class = ProductCommentSerializer


class ProductCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        user = User.objects.get(phone=request.user.phone)
        shop = Shop.objects.get(user=user)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(shop=shop)
        return Response(ProductSerializer(new_serializer).data)

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-priority')[0:100]
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        parameters = request.GET.dict()
        all_products = Product.objects.all()
        if "category" in parameters:
            all_products = all_products.filter(category=parameters["category"])
        elif "price" in parameters:
            if parameters["price"]=="price":
                all_products = all_products.order_by('price')
            else:
                all_products = all_products.order_by('-price')
        elif "off" in parameters:
            if parameters["off"]=="off":
                all_products = all_products.order_by('off')
            else:
                all_products = all_products.order_by('-off')
        all_products = all_products.order_by('-priority').order_by('?')[0:100]
        return Response(ProductSerializer(all_products, many=True).data, status=200)

class ProductRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        user = User.objects.get(phone=request.user.phone)
        shop = Shop.objects.get(user=user)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(shop=shop)
        return Response(ProductSerializer(new_serializer).data)

class ShopCreate(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ShopSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user=request.user)
        return Response(ShopSerializer(new_serializer).data)

class ShopList(generics.ListAPIView):
    queryset = Shop.objects.all().order_by('-priority')[0:100]
    serializer_class = ShopSerializer

class ShopRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopProductList(generics.GenericAPIView):
     
    def get(self, request, *args,  **kwargs):
        pk = kwargs["pk"]
        shop = Shop.objects.filter(pk=pk).first()
        products = Product.objects.filter(shop=shop)
        serializer = ProductShowSerializer(products, many=True)
        return Response(serializer.data)

class CategoryCreate(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class CategoryRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class ProductSearch(generics.GenericAPIView):
    serializer_class = ProductSearchSeralizer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        search = serializer.data["name"]       
        queryset = Product.objects.annotate(
        similarity=TrigramSimilarity('name', search)).filter(similarity__gt=0.3).order_by('-similarity')
        return Response(ProductSerializer(queryset, many=True).data)

class ShopSearch(generics.GenericAPIView):
    serializer_class = ShopSearchSeralizer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        search = serializer.data["name"]        
        queryset = Shop.objects.annotate(
        similarity=TrigramSimilarity('name', search)).filter(similarity__gt=0.3).order_by('-similarity')
        return Response(ShopSerializer(queryset, many=True).data)
