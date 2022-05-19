from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from order.models import(
    Order, UsedSms, UsedBanner,
    UsedRecommendedProduct, UsedRecommendedShop
)
from order.serializer import(
    OrderSerializer, UsedBannerSerializer,
    UsedRecommendedProductSerializer, UsedRecommendedShopSerializer,
    UsedSmsSerializer
)

class OrderCreate(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user=request.user)
        return Response(OrderSerializer(new_serializer).data)

class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Order.objects.all()
    serializer_class =  OrderSerializer
    
class UsedRecommendedProductCreate(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = UsedRecommendedProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user=request.user)
        return Response(UsedRecommendedProductSerializer(new_serializer).data)

class UsedRecommendedProductList(generics.ListAPIView):
    queryset = UsedRecommendedProduct.objects.all()
    serializer_class = UsedRecommendedProductSerializer

class UsedRecommendedProductRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsedRecommendedProduct.objects.all()
    serializer_class =  UsedRecommendedProductSerializer
    
class UsedRecommendedShopCreate(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = UsedRecommendedShopSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user=request.user)
        return Response(UsedRecommendedShopSerializer(new_serializer).data)

class UsedRecommendedShopList(generics.ListAPIView):
    queryset = UsedRecommendedShop.objects.all()
    serializer_class = UsedRecommendedShopSerializer

class UsedRecommendedShopRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsedRecommendedShop.objects.all()
    serializer_class = UsedRecommendedShopSerializer

class UsedBannerCreate(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = UsedBannerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user=request.user)
        return Response(UsedBannerSerializer(new_serializer).data)

class UsedBannerList(generics.ListAPIView):
    queryset = UsedBanner.objects.all()
    serializer_class = UsedBannerSerializer

class UsedBannerRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsedBanner.objects.all()
    serializer_class =  UsedBannerSerializer

class UsedSmsCreate(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = UsedSmsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user=request.user)
        return Response(UsedSmsSerializer(new_serializer).data)

class UsedSmsList(generics.ListAPIView):
    queryset = UsedSms.objects.all()
    serializer_class = UsedSmsSerializer

class UsedSmsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsedSms.objects.all()
    serializer_class = UsedSmsSerializer
