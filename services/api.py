from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from .models import(
    SmsPack,
    BannerPack,
    RecommendedProductPack, 
    RecommendedShopPack, 
)
from .serializer import(
    SmsPackSerializer,
    BannerPackSerializer,
    RecommendedProductSerializer, 
    RecommendedShopPackSerializer, 
)

class RecommendedShopPackCreate(generics.CreateAPIView):
    serializer_class = RecommendedShopPackSerializer
    permission_classes = []

class RecommendedShopPackList(generics.ListAPIView):
    queryset = SmsPack.objects.all()
    serializer_class = RecommendedShopPackSerializer

class RecommendedShopPackRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecommendedShopPack.objects.all()
    serializer_class = RecommendedShopPackSerializer

class RecommendedProductPackCreate(generics.CreateAPIView):
    serializer_class = RecommendedProductSerializer
    permission_classes = []

class RecommendedProductPackList(generics.ListAPIView):
    queryset = SmsPack.objects.all()
    serializer_class = RecommendedProductSerializer

class RecommendedProductPackRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecommendedProductPack.objects.all()
    serializer_class = RecommendedProductSerializer

class SmsPackCreate(generics.CreateAPIView):
    serializer_class = SmsPackSerializer
    permission_classes = []

class SmsPackList(generics.ListAPIView):
    queryset = SmsPack.objects.all()
    serializer_class = SmsPackSerializer

class SmsPackRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = SmsPack.objects.all()
    serializer_class = SmsPackSerializer

class BannerPackCreate(generics.CreateAPIView):
    serializer_class = BannerPackSerializer
    permission_classes = []

class BannerPackList(generics.ListAPIView):
    queryset = BannerPack.objects.all()
    serializer_class = BannerPackSerializer

class BannerPackRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BannerPack.objects.all()
    serializer_class = BannerPackSerializer
