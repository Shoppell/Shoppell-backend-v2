from email.policy import HTTP
import imp
from jmespath import search
# from yaml import serialize
from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from django.http import JsonResponse
from .serializer import ShopSerializer, ProductSerializer, CategorySerializer, ProductSearchSeralizer, ShopSearchSeralizer
from user_auth.models import User
from .models import Product, Shop, Category
from rest_framework.permissions import IsAuthenticated
from django.contrib.postgres.search import TrigramSimilarity
from django.contrib.postgres.operations import TrigramExtension
from django.db.models import Q

class ProductCreate(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProductRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ShopCreate(generics.CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]

class ShopList(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]

class ShopRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    # permission_classes = [IsAuthenticated]

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

    def get(self, request, *args,  **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        search = serializer.data["name"]        

        queryset = Product.objects.get(name__contains=search)

        return Response(ProductSerializer(queryset).data)
        

class ShopSearch(generics.GenericAPIView):
    serializer_class = ShopSearchSeralizer

    def get(self, request, *args,  **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        search = serializer.data["name"]        

        queryset = Shop.objects.get(name__contains=search)
    
        return Response(ShopSerializer(queryset).data)
