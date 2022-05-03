from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from .models import SmsPack, BannerPack, ReportProduct, ReportShop, Ticket, IPAddress, DailyProductView, DailyShopView, CartBanner, CartSms, Order, UsedBanner, UsedSms
from .serializer import SmsPackSerializer, BannerPackSerializer, ReportProductSerializer, ReportShopSerializer, TicketSerializer, IPAddressSerializer, DailyProductViewSerializer, DailyShopViewSerializer, CartBannerSerializer, CartSmsSerializer, OrderSerializer, UsedBannerSerializer, UsedSmsSerializer


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

class ReportProductCreate(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = ReportProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user=request.user)
        return Response(ReportProductSerializer(new_serializer).data)

class ReportProductList(generics.ListAPIView):
    queryset = ReportProduct.objects.all()
    serializer_class = ReportProductSerializer

class ReportProductRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReportProduct.objects.all()
    serializer_class = ReportProductSerializer

class ReportShopCreate(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = ReportShopSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user=request.user)
        return Response(ReportShopSerializer(new_serializer).data)

class ReportShopList(generics.ListAPIView):
    queryset = ReportShop.objects.all()
    serializer_class = ReportShopSerializer

class ReportShopRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReportShop.objects.all()
    serializer_class = ReportShopSerializer

class TicketCreate(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user=request.user)
        return Response(TicketSerializer(new_serializer).data)

class TicketList(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class IPAddressCreate(generics.CreateAPIView):
    serializer_class = IPAddressSerializer
    permission_classes = []

class IPAddressList(generics.ListAPIView):
    queryset = IPAddress.objects.all()
    serializer_class = IPAddressSerializer

class IPAddressRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = IPAddress.objects.all()
    serializer_class = IPAddressSerializer

class DailyProductViewCreate(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = DailyProductViewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user_ip=request.user.ip_address)
        return Response(DailyProductViewSerializer(new_serializer).data)

class DailyProductViewList(generics.ListAPIView):
    queryset = DailyProductView.objects.all()
    serializer_class = DailyProductViewSerializer

class DailyProductViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyProductView.objects.all()
    serializer_class = DailyProductViewSerializer

class DailyShopViewCreate(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = DailyShopViewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user_ip=request.user.ip_address)
        return Response(DailyShopViewSerializer(new_serializer).data)

class DailyShopViewList(generics.ListAPIView):
    queryset = DailyShopView.objects.all()
    serializer_class = DailyShopViewSerializer

class DailyShopViewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyShopView.objects.all()
    serializer_class = DailyShopViewSerializer

class CartBannerCreate(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = CartBannerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user=request.user)
        return Response(CartBannerSerializer(new_serializer).data)

class CartBannerList(generics.ListAPIView):
    queryset = Ticket.objects.all()
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

class OrderCreate(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_serializer = serializer.save(user=request.user)
        return Response(OrderSerializer(new_serializer).data)

class OrderList(generics.ListAPIView):
    queryset = CartSms.objects.all()
    serializer_class = CartSmsSerializer

class OrderRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Order.objects.all()
    serializer_class =  OrderSerializer
    
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
