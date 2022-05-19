from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from cart.serializers import(
    CartRecommendedProduct, CartRecommendedShop,
    CartRecommendedProductSerializer, CartRecommendedShopSerializer,
    CartBannerSerializer, CartSmsSerializer,
)
from cart.models import(
    CartSms, CartBanner,
    CartRecommendedProduct, CartRecommendedShop
)

class CartRecommendedShopCreate(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = CartRecommendedShopSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user=request.user)
        return Response(CartRecommendedShopSerializer(new_serializer).data)

class CartRecommendedShopList(generics.ListAPIView):
    queryset = CartRecommendedShop.objects.all()
    serializer_class = CartRecommendedShopSerializer

class CartRecommendedShopRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartRecommendedShop.objects.all()
    serializer_class = CartRecommendedShopSerializer

class CartRecommendedProductCreate(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = CartRecommendedProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user=request.user)
        return Response(CartRecommendedProductSerializer(new_serializer).data)

class CartRecommendedProductList(generics.ListAPIView):
    queryset = CartRecommendedProduct.objects.all()
    serializer_class = CartRecommendedProductSerializer

class CartRecommendedProductRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartRecommendedProduct.objects.all()
    serializer_class = CartRecommendedProductSerializer


class CartBannerCreate(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = CartBannerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user=request.user)
        return Response(CartBannerSerializer(new_serializer).data)

class CartBannerList(generics.ListAPIView):
    queryset = CartBanner.objects.all()
    serializer_class = CartBannerSerializer

class CartBannerRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartBanner.objects.all()
    serializer_class = CartBannerSerializer

class CartSmsCreate(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = CartSmsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user=request.user)
        return Response(CartSmsSerializer(new_serializer).data)

class CartSmsList(generics.ListAPIView):
    queryset = CartSms.objects.all()
    serializer_class = CartSmsSerializer

class CartSmsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartSms.objects.all()
    serializer_class = CartSmsSerializer
