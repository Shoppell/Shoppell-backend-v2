from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer, LoginSerializer
from .models import User
from django.contrib.auth import login
from user_auth import helper
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

class UserRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class LoginApi(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args,  **kwargs):
        user = User.objects.first()
        refresh = RefreshToken.for_user(user)
        print(type(refresh))
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = request.session['user_mobile']
        otp = serializer.data['otp']
        response = Response()
        try:
            user = User.objects.get(mobile=mobile)
            if user.otp == otp:
                user.otp = None
                user.last_login = timezone.now()
                user.save()
                refresh = RefreshToken.for_user(user)
                response.set_signed_cookie(
                       key = 'ACCESS_TOKEN', 
                       value = str(refresh.access_token),
                )
                login(request, user)
                response.data = {"refresh" : str(refresh),"access":str(refresh.access_token)}
                return response
            else:
                return Response({"No User" : "Invalid otp OR No any active user found for given otp"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"Time out" : "Given otp is expired!!"}, status=status.HTTP_408_REQUEST_TIMEOUT)


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data['mobile']
        request.session['user_mobile'] = mobile
        try:
            user = User.objects.get(mobile=mobile)
            otp = helper.otp_generator()
            helper.send_otp(mobile, otp)
            user.otp = otp
            user.otp_create_time = timezone.now
            user.save()
            return Response({
                "message": "verify it",
            })
        except User.DoesNotExist:
            serializer.save()
        
            return Response({
                "message": "User Created Successfully.  Now verify it",
            })
