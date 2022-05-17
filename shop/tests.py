from shoppell.tests import ShoppellAPIClient, ShoppellTestCase
from django.urls import reverse
from rest_framework import status
from user_auth.models import User

class UserTest(ShoppellTestCase):

    fixtures = [
        "shop/fixtures/shop_fixtures.yaml",
        "user_auth/fixtures/user_fixtures.yaml",
    ]

    def setUp(self):
        super().setUp()
        return

    def test_create_shop(self):
        user_data = {
            "name":"shop",
            "slug":"shop1",  
        }
        
        response = self.client.post(reverse("shop:shop_create"), data=user_data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.filter().first()
        

