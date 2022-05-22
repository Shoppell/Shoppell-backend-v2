from asyncore import read
from rest_framework import serializers
from .models import Shop, Product, Category, SavedProduct, ProductComment, ShopComment
from user_auth.serializer import UserSerializer


class SavedProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = SavedProduct
        fields = '__all__'
        
class ShopCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = ShopComment
        fields = '__all__'

class ProductCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = ProductComment
        fields = '__all__'

class ProductSearchSeralizer(serializers.Serializer):
    name = serializers.CharField(max_length=20)

class ShopSearchSeralizer(serializers.Serializer):
    name = serializers.CharField(max_length=20)

class ShopSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Shop
        fields = '__all__'

class ShopShowSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Shop
        exclude = ['created', 'modified', 'is_ban']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price','image1', 'last_price', 'off', 'category', 'rating']

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
