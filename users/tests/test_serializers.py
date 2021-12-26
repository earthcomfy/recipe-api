from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegisterationSerializerTest(APITestCase):
    def setUp(self):
        self.username = 'testuser'
        self.email = 'kk@kk.com'
        self.password = '12three'

    def test_register_user(self):
        """
        Ensure we can create a new user.
        """
        url = reverse('users:create-user')
        data = {
            'username': self.username,
            'email': self.email,
            'password': self.password
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED, response.content)
        self.assertEqual(User.objects.count(), 1)
