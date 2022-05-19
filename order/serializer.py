from rest_framework import serializers
from user_auth.serializer import UserSerializer
from order.models import(
    Order, UsedBanner, UsedSms,
    UsedRecommendedShop, UsedRecommendedProduct
)

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
        