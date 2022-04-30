from django.urls import path
from user_auth import api

urlpatterns = [
    path('register', api.RegisterApi.as_view()),
    path('verify', api.LoginApi.as_view()),
    path('rud/<int:pk>', api.UserRUD.as_view()),
    path('gateway/', api.GoToGatewayShop.as_view()),
    path('callback/', api.CallbackGatewayShop.as_view(), name='callback'),
  
]
