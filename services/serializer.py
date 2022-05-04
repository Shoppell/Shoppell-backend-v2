from rest_framework import serializers
from user_auth.serializer import UserSerializer
from .models import SmsPack, BannerPack, ReportShop, ReportProduct, Ticket, IPAddress, DailyProductView, DailyShopView, CartBanner, CartSms, Order, UsedBanner, UsedSms, RecommendedProductPack, RecommendedShopPack, CartRecommendedProduct, CartRecommendedShop, UsedRecommendedShop, UsedRecommendedProduct

class SmsPackSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = SmsPack
        fields = '__all__'

class BannerPackSerializer(serializers.ModelSerializer):

    class Meta:
        model = BannerPack
        fields = '__all__'

class RecommendedProductSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = RecommendedProductPack
        fields = '__all__'

class RecommendedShopPackSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecommendedShopPack
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

class CartRecommendedProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CartRecommendedProduct
        fields = '__all__'

class CartRecommendedShopSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CartRecommendedShop
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

class UsedBannerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UsedBanner
        fields = '__all__'

class UsedSmsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UsedSms
        fields = '__all__'
        
class UsedRecommendedShopSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UsedRecommendedShop
        fields = '__all__'

class UsedRecommendedProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UsedRecommendedProduct
        fields = '__all__'
        