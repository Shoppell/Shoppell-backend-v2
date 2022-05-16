from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer, LoginSerializer, GateSerializer
from .models import User
from django.contrib.auth import login
from user_auth import helper
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException
from django.http import HttpResponse, Http404
from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
import logging
from rest_framework.views import APIView
import secrets
# def callback_gateway_shop(request):
#     
from django.contrib.sessions.backends.db import SessionStore

class CallbackGatewayShop(APIView):

    def get(self, request, *args,  **kwargs):
        tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
        if not tracking_code:
            logging.debug("این لینک معتبر نیست.")
            raise Http404

        try:
            bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
        except bank_models.Bank.DoesNotExist:
            logging.debug("این لینک معتبر نیست.")
            raise Http404

        # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
        if bank_record.is_success:
            # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
            # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
            if request.user.is_authenticated:
                request.user.cash += request.user.cash
            return HttpResponse("موفق")
            # product_registered_customer(request.user.mobile, 'shopeton.ir/bought/')

            # return redirect('bought')

        # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
        return HttpResponse("پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")

class GoToGatewayShop(generics.GenericAPIView):
    serializer_class = GateSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        amount = serializer.data["cash"]*10
        factory = bankfactories.BankFactory()
        try:
            bank = factory.auto_create() # or factory.create(bank_models.BankType.BMI) or set identifier
            bank.set_request(request)
            bank.set_amount(amount)
            # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
            bank.set_client_callback_url(reverse('callback'))
            # bank.set_mobile_number(user_mobile_number)  # اختیاری
        
            # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
            # پرداخت برقرار کنید. 
            bank_record = bank.ready()
            
            # هدایت کاربر به درگاه بانک
            return bank.redirect_gateway()
        except AZBankGatewaysException as e:
            logging.critical(e)
            # TODO: redirect to failed page.
            raise e


class UserRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class LoginApi(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args,  **kwargs):
        user = User.objects.first()
        refresh = RefreshToken.for_user(user)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        verifyCode = serializer.data['verifyCode']
        phone = serializer.data['phone']
        response = Response()
        try:
            user = User.objects.get(phone=phone)
            if user.verifyCode == verifyCode:
                user.verifyCode = None
                user.last_login = timezone.now()
                user.save()
                refresh = RefreshToken.for_user(user)
                response.set_signed_cookie(
                       key = 'ACCESS_TOKEN', 
                       value = str(refresh.access_token),
                )
                login(request, user)
                owner = False
                if request.user.is_shop_owner:
                    owner = True
                response.data = {"refresh" : str(refresh),"access":str(refresh.access_token), "owner":owner}
                return response
            else:
                return Response({"No User" : "Invalid verifyCode OR No any active user found for given verifyCode"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"Not Found" : "No user with this number!!"}, status=status.HTTP_408_REQUEST_TIMEOUT)


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data['phone']
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            user = User.objects.create(phone=phone, password=secrets.token_urlsafe(10))
        verifyCode = helper.verifyCode_generator()
        helper.send_verifyCode(phone, verifyCode)
        user.verifyCode = verifyCode
        user.verifyCode_create_time = timezone.now
        user.save()
        return Response({
                "message": "Ok, verify it",
        })
