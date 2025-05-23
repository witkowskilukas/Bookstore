from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView

class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template_used(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_contains_incorrect_html(self):
        self.assertNotContains(self.response, "ala lepi pierogi")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')     #view przekształca adres url i zwraca powiązany z nim view
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )

class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_url_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_aboutpage_template_used(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_contains_incorrect_html(self):
        self.assertNotContains(self.response, "ala lepi pierogi")

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')     #view przekształca adres url i zwraca powiązany z nim view
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )