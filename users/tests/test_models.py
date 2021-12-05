from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class RecipeCategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="testuser", email='kk@kk.com', password='12three')

    def test_string_representation(self):
        user = User.objects.get(id=1)
        expected_string = user.email
        self.assertEqual(str(user), expected_string)
