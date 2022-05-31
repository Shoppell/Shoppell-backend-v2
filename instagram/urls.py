from django.urls import path
from instagram import api

app_name = 'instagram'

urlpatterns = [
    path('account/create/', api.InstagramAccountCloneView.as_view()),

]
