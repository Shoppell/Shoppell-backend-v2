from user_auth.serializer import UserSerializer
from rest_framework import serializers
from util.models import (
    ReportProduct, ReportShop, 
    Ticket, IPAddress, 
    DailyProductView, DailyShopView
)

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
