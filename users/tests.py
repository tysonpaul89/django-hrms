from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='jack',
            email='jack@m.com',
            password='pass'
        )
        self.assertEqual(user.username, 'jack')
        self.assertEqual(user.email, 'jack@m.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='jill',
            email='jill@m.com',
            password='pass'
        )
        self.assertEqual(user.username, 'jill')
        self.assertEqual(user.email, 'jill@m.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)