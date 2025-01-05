from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve


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


class SignupPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, template_name='account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Bla bla')
    

    
    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)