from rest_framework import serializers
from .models import User
import secrets
from user_auth import helper
from django.utils import timezone

class LoginSerializer(serializers.Serializer):
    otp = serializers.IntegerField()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('mobile', )
    
    def create(self, validated_data):
        created_password = secrets.token_urlsafe(9)
        otp = helper.otp_generator()
        mobile_number = validated_data['mobile']
        helper.send_otp(mobile_number, otp)
        user = User.objects.create(mobile=mobile_number,password = created_password,otp=otp,otp_create_time=timezone.now)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
