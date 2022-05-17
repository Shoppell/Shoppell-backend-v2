from typing import Optional

from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from user_auth.models import User

USER_FIXTURE_ADDRESS = "user_auth/fixtures/user_fixtures.yaml"


class ShoppellAPIClient(APIClient):

    def credentials(self, user: User, http_authorization_header: str = "Bearer ", **kwargs):
        access_token = AccessToken.for_user(user)
        access = str(access_token)
        super().credentials(HTTP_AUTHORIZATION=http_authorization_header + access, **kwargs)
        return

class ShoppellTestCase(APITestCase):
    client_class = ShoppellAPIClient
    fixtures = [
        "user_auth/fixtures/user_fixtures.yaml",
    ]
    client_phone: Optional[str] = "09930731973"

    def setUp(self) -> None:
        self.user = User.objects.get(phone=self.client_phone)
        self.client.credentials(user=self.user)
        # if USER_FIXTURE_ADDRESS in self.fixtures and self.client_phone:
        #     self.user = User.objects.get(username=self.client_phone)
        #     self.client.credentials(user=self.user)
