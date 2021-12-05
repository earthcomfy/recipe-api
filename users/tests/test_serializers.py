from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterationSerializerTest(APITestCase):
    def test_register_user(self):
        """
        Ensure we can create a new user.
        """
        url = reverse('users:create_user')
        data = {'username': 'testuser',
                'email': 'kk@kk.com', 'password': "12three"}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
