from shoppell.tests import ShoppellAPIClient, ShoppellTestCase
from django.urls import reverse
from rest_framework import status
from user_auth.models import User

class UserTest(ShoppellTestCase):

    fixtures = [
        "user_auth/fixtures/user_fixtures.yaml",
    ]

    def setUp(self):
        super().setUp()
        return

    #be careful of this test
    def test_register_user(self):
        user_data = {
            "phone": "09930731973",
        }
        response = self.client.post(reverse("user_auth:register"), data=user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("09930731973", User.objects.filter().first().phone)

    # this test must run with top test
    def test_verify_user(self):
        user_data = {
            "verifyCode": 1243,
            "phone": str(user.phone),
        }
        response = self.client.post(reverse("user_auth:verify"), data=user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.filter().first().verifyCode, 1243)
