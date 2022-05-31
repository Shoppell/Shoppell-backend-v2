from datetime import datetime
from email.mime import image
from pydoc import describe
import instaloader
from logging import raiseExceptions
from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from instagram.serializer import InstagramAccount
from shop.models import Category, Shop, Product
import requests


class InstagramAccountCloneView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = InstagramAccount(data=request.data)
        serializer.is_valid(raiseExceptions)
        username = serializer.validated_data["username"]
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context, username)
        try:
            shop = Shop.objects.create(user=request.user, name=username, slug=username, description=profile.biography)
        except: 
            shop = Shop.objects.create(user=request.user, name=username, description=profile.biography)
        shop.get_image_from_url(profile.profile_pic_url)
        num = 0
        for post in profile.get_posts():
            if not post.is_video:
                if num>4:
                    break
                product = Product.objects.create(shop=shop, name=shop.name, description=post.caption, price=100, last_price=80, category=Category.objects.first())
                for x in post.get_sidecar_nodes(start=0, end=-1):
                    product.get_image_from_url(x.display_url)
                num += 1

        return Response({
                "message": "Ok, Cloned",
        }, status=status.HTTP_200_OK) 

