from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):

    def test_createuser(self):
        User = get_user_model()
        test_user = User.objects.create(
            username="Lukas",
            email='lukas@gmail.com',
            password='lukas'
        )

        self.assertEqual(test_user.username, 'Lukas')
        self.assertEqual(test_user.email, 'lukas@gmail.com')
        self.assertTrue(test_user.is_active)
        self.assertFalse(test_user.is_staff)
        self.assertFalse(test_user.is_superuser)
    
    def test_createsuperuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="John",
            email='john@gmail.com',
            password='john'
        )

        self.assertEqual(admin_user.username, 'John')
        self.assertEqual(admin_user.email, 'john@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
    
    