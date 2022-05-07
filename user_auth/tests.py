from shoppell.tests import ShoppellAPIClient, ShoppellTestCase
from django.urls import reverse
from rest_framework import status

# class UserTest(ShoppellTestCase):

#     fixtures = [
#         "user_auth/fixtures/user_fixtures.yaml",
#     ]

#     def setUp(self):
#         super().setUp()
#         self.dummy_namespace = Namespace.objects.exclude(id__in=self.user.namespaces.all().values("id")).first()
#         return

#     def Test_create_user(self):
#         patient_data = {
#             "first_name": "Nate",
#             "last_name": "River",
#             "mobile": "09930731973",
#             "password": "navid1381",
      
#         }
#         response = self.client.post(reverse("user_auth:register"), data=patient_data)
#         resp_dict = response.json()
#         print(resp_dict)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # for field in patient_data:
        #     self.assertEqual(patient_data[field], resp_dict[field])

        # return resp_dict["id"]

