from rest_framework import serializers
from user_auth.serializer import UserSerializer
from .models import SmsPack, BannerPack, ReportShop, ReportProduct, Ticket, IPAddress, DailyProductView, DailyShopView, CartBanner, CartSms, Order

class SmsPackSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = SmsPack
        fields = '__all__'

class BannerPackSerializer(serializers.ModelSerializer):

    class Meta:
        model = BannerPack
        fields = '__all__'

class ReportShopSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ReportShop
        fields = '__all__'

class ReportProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ReportProduct
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'

class IPAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = IPAddress
        fields = '__all__'

class DailyProductViewSerializer(serializers.ModelSerializer):
    user_ip = IPAddressSerializer(read_only=True)

    class Meta:
        model = DailyProductView
        fields = '__all__'

class DailyShopViewSerializer(serializers.ModelSerializer):
    user_ip = IPAddressSerializer(read_only=True)

    class Meta:
        model = DailyShopView
        fields = '__all__'

class CartBannerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CartBanner
        fields = '__all__'

class CartSmsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CartSms
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        