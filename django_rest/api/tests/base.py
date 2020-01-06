from django.urls import reverse
from django.contrib import auth
from rest_framework.test import APITestCase


class APIBaseTestCase(APITestCase):
    def api_login(self, username, password):
        """
        Call auth.login endpoint to authenticate
        user.
        """
        url = reverse('auth.login')
        data = {
            'username': username,
            'password': password,
        }
        response = self.client.post(url, data, format='json')
        user = auth.get_user(self.client)
        self.assertEqual(user.is_authenticated, True)
        return response

    def api_logout(self):
        """
        Call auth.logout endpoint to logout user.
        """
        url = reverse('auth.logout')
        response = self.client.post(url, {}, format='json')
        user = auth.get_user(self.client)
        self.assertEqual(user.is_authenticated, False)
        return response
