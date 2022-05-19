from rest_framework import serializers
from user_auth.serializer import UserSerializer
from .models import(
    SmsPack, BannerPack,
    RecommendedProductPack, RecommendedShopPack,
) 

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
