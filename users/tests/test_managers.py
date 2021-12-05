from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserManagerTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username="testuser",
            email='kk@kk.com',
            password='12three')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'kk@kk.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(username='')
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="12three")

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            username="testuser",
            email='kk@kk.com',
            password='12three')
        self.assertEqual(admin_user.username, 'testuser')
        self.assertEqual(admin_user.email, 'kk@kk.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='kk@kk.com', password='12three', is_superuser=False)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='kk@kk.com', password='12three', is_staff=False)
