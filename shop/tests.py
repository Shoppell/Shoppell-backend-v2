from shoppell.tests import ShoppellAPIClient, ShoppellTestCase
from django.urls import reverse
from rest_framework import status
from user_auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
import pathlib
import os

class ShopTest(ShoppellTestCase):

    fixtures = [
        "shop/fixtures/shop_fixtures.yaml",
        "user_auth/fixtures/user_fixtures.yaml",
    ]

    def setUp(self):
        super().setUp()
        return

    def not_test_create_shop(self):
        shop_data = {
            "name":"shop",
            "slug":"shop1",  
        }
        
        response = self.client.post(reverse("shop:shop_create"), data=shop_data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # user = User.objects.filter().first()
    

class ProductTest(ShoppellTestCase):

    fixtures = [
        "shop/fixtures/shop_fixtures.yaml",
        "user_auth/fixtures/user_fixtures.yaml",
    ]

    def setUp(self):
        super().setUp()
        return
    
    def test_product_create(self):
        # print(os.getcwd())
        # print(pathlib.Path("banner2.jpg"))
        file = File(open("media/products/banner2.jpg", "rb"))
        uploaded_file = SimpleUploadedFile("banner2.jpg", file.read(), content_type="multipart/form-data")
        product_data = {
            "name":"product",
            "image1":uploaded_file,
            "price":12324,
            "last_price":244,
        }
        response = self.client.post(reverse("shop:product_create"), data=product_data, format="multipart",)
        # print(response.json())
        self.assertEqual(response.status_code, 201)

