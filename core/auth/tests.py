from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class AuthenticationTest(APITestCase):
    base_url_login = reverse("core:auth-login-list")
    base_url_refresh = reverse("core:auth-refresh-list")

    data_login = {
        "email": "testuser@yopmail.com",
        "password": "12345678",
    }

    def test_login(self):
        response = self.client.post(f"{self.base_url_login}", data=self.data_login)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_refresh(self):
        # Login

        response = self.client.post(f"{self.base_url_login}", data=self.data_login)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()

        access_token = response_data.get('access')
        refresh_token = response_data.get('refresh')

        # Refreshing the token

        response = self.client.post(f"{self.base_url_refresh}", data={
            "refresh": refresh_token
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertNotEqual(access_token, response_data.get('access'))
