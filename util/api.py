from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from util.models import(
    ReportShop, ReportProduct, Ticket,
    IPAddress, DailyProductView, DailyShopView
)

from util.serializer import(
    ReportProductSerializer, ReportShopSerializer, TicketSerializer, 
    DailyShopViewSerializer, DailyProductViewSerializer, IPAddressSerializer
)

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

