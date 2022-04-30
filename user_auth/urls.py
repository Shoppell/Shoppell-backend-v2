from django.urls import path
from user_auth import api

urlpatterns = [
    path('register', api.RegisterApi.as_view()),
    path('verify', api.LoginApi.as_view()),
    path('rud/<int:pk>', api.UserRUD.as_view()),
]
