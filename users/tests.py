from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
            shipping_address='123 Test Street'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('testpassword'))
        self.assertEqual(user.shipping_address, '123 Test Street')

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            username='adminuser',
            email='adminuser@example.com',
            password='adminpassword'
        )
        self.assertEqual(admin_user.username, 'adminuser')
        self.assertEqual(admin_user.email, 'adminuser@example.com')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
