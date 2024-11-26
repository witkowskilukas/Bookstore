from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignUpView

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

class SignUpViewTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign up')
        self.assertNotContains(self.response, "ege czege")

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignUpView.as_view().__name__)


    
    