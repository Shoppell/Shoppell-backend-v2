from django.urls import URLPattern, path
from user_auth import api

urlpatterns = [
    path('register', api.RegisterApi.as_view()),
    path('verify', api.LoginApi.as_view()),
    path('rud', api.UserRUD.as_view()),
]
