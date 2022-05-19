from rest_framework import serializers
from user_auth.serializer import UserSerializer
from cart.models import(
    CartBanner, CartSms,
    CartRecommendedShop, CartRecommendedProduct
)

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
