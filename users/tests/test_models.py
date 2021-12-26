from django.test import TestCase
from django.contrib.auth import get_user_model

from .factories import UserFactory, ProfileFactory


User = get_user_model()


class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_string_representation(self):
        user = self.user
        expected_string = user.email
        self.assertEqual(str(user), expected_string)


class ProfileModelTest(TestCase):
    def setUp(self):
        self.profile = ProfileFactory()

    def test_string_representation(self):
        profile = self.profile
        expected_string = profile.user.username
        self.assertEqual(str(profile), expected_string)
