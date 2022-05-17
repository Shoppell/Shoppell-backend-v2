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
        user = User.objects.filter().first()

    # this test must run with top test
    def test_verify_user(self):
        user = User.objects.filter().first()
        user_data = {
            "verifyCode": user.verifyCode,
            "phone": str(user.phone),
        }
        response = self.client.post(reverse("user_auth:verify"), data=user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
