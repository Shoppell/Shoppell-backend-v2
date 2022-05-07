from typing import Optional

from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from user_auth.models import User

USER_FIXTURE_ADDRESS = "user_auth/test_fixtures/user_fixtures.yaml"


class ShoppellAPIClient(APIClient):

    def credentials(self, user: User, http_authorization_header: str = "Bearer ", **kwargs):
        access_token = AccessToken.for_user(user)
        access = str(access_token)
        super().credentials(HTTP_AUTHORIZATION=http_authorization_header + access, **kwargs)
        return

class ShoppellTestCase(APITestCase):
    client_class = ShoppellAPIClient
    fixtures = [USER_FIXTURE_ADDRESS]
    client_username: Optional[str] = "user_test"

    def setUp(self) -> None:
        if USER_FIXTURE_ADDRESS in self.fixtures and self.client_username:
            self.user = User.objects.get(username=self.client_username)
            self.client.credentials(user=self.user)
