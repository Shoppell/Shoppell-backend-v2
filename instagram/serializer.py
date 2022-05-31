from rest_framework import serializers
# from .models import Shop, Product
# from user_auth.serializer import UserSerializer

class InstagramAccount(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    