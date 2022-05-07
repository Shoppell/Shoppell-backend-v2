# from shoppell.tests import ShoppellAPIClient, SynappsAPITestCase
# from django.urls import reverse
# from rest_framework import status


# class PatientTest(SynappsAPITestCase):

#     fixtures = [
#         "user_auth/fixtures/user_fixtures.yaml",
#         # "location/fixtures/countries.yaml",
#         # "location/fixtures/iran_adm_divisions.yaml",
#         # "clinic/test_fixtures/clinic_fixture.yaml",
#         # "patient/test_fixtures/patient_fixture.yaml",
#     ]

#     def setUp(self):
#         super().setUp()
#         # self.dummy_namespace = Namespace.objects.exclude(id__in=self.user.namespaces.all().values("id")).first()
#         return

#     def Test_create(self):
#         patient_data = {
#             "first_name": "Nate",
#             "last_name": "River",
#             "gender": "M",
#             "national_id": "2069812345",
#             "has_national_id": True,
#             "namespace": 7357,
#             "note": "blah blah blah",
#             "nationality": "US",
#             "marital_status": "S",
#             "birth_location": 12,
#             "dob": "1991-04-10",
#         }
#         response = self.client.post(reverse("patients:create_search"), data=patient_data)
#         resp_dict = response.json()
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         for field in patient_data:
#             self.assertEqual(patient_data[field], resp_dict[field])

#         return resp_dict["id"]

    # def Test_delete(self, patient_id):
    #     response = self.client.delete(reverse("patients:get_put_del_patient", args=[str(patient_id)]))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     response = self.client.get(reverse("patients:get_put_del_patient", args=[str(patient_id)]))
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def Test_put(self, patient_id):
    #     new_values = {
    #         "first_name": "Teru",
    #         "last_name": "Mikami",
    #         "note": "different blah blah blah",
    #         "nationality": "JP",
    #         "dob": "1982-06-07",
    #     }
    #     response = self.client.put(
    #         reverse("patients:get_put_del_patient", args=[str(patient_id)]),
    #         data=new_values,
    #     )

    #     resp_dict = response.json()
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     for field in new_values:
    #         self.assertEqual(new_values[field], resp_dict[field])

    # def test_create_and_delete(self):
    #     patient_id = self.Test_create()
    #     self.Test_put(patient_id)
    #     self.Test_delete(patient_id)

    # def test_create_incognito_patient(self):
    #     patient_data = {
    #         "incognito": True,
    #         "namespace": 7357,
    #     }
    #     response = self.client.post(reverse("patients:create_search"), data=patient_data)
    #     resp_dict = response.json()
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     for field in patient_data:
    #         self.assertEqual(patient_data[field], resp_dict[field])

    # def test_create_inaccessible_namespaces(self):
    #     patient_data = {
    #         "incognito": True,
    #         "namespace": self.dummy_namespace.id,
    #     }
    #     response = self.client.post(reverse("patients:create_search"), data=patient_data)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def test_RUD_patient_inaccessible_namespace(self):
    #     patient = Patient.objects.create(incognito=True, namespace=self.dummy_namespace)
    #     response = self.client.get(reverse("patients:get_put_del_patient", args=[str(patient.id)]))
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    #     response = self.client.put(reverse("patients:get_put_del_patient", args=[str(patient.id)]))
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    #     response = self.client.delete(reverse("patients:get_put_del_patient", args=[str(patient.id)]))
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def test_patient_statistic_Get(self):
    #     day_data = {
    #         "start": "2015-02-25",
    #         "end": "2023-02-28",
    #         "namespace": 7357,
    #     }
    #     response = self.client.get(reverse("patients:patient_statistics"), data=day_data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
