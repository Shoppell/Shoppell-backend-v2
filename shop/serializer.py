from attr import field
from rest_framework import serializers
from .models import Shop, Product, Category

class ProductSearchSeralizer(serializers.Serializer):
    name = serializers.CharField(max_length=20)

class ShopSearchSeralizer(serializers.Serializer):
    name = serializers.CharField(max_length=20)


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
