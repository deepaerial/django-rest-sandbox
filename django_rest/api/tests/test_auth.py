from rest_framework import status

from api.tests import base
from user.factories import UserFactory


class APIAuthTestCase(base.APIBaseTestCase):
    def setUp(self):
        self.user = UserFactory(password="password")

    def test_login(self):
        """
        Testing api login endpoint
        """
        response = self.api_login(self.user.username, "password")
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('username', json_response)
        self.assertIn('email', json_response)

    def test_logout(self):
        """
        Testing api logout endpoint
        """
        response = self.api_logout()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.api_login(self.user.username, "password")
        response = self.api_logout()
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', json_response)
