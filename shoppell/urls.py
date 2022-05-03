from django.contrib import admin
from django.urls import path, include
from user_auth.api import RegisterApi, LoginApi
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from shoppell import settings
from shop import api
from azbankgateways.urls import az_bank_gateways_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/services/', include('services.urls')),
    path('api/v1/shop/', include('shop.urls')),
    path('api/v1/user/', include('user_auth.urls')),
    path('bankgateways/', az_bank_gateways_urls()),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)