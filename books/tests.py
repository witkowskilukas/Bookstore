from django.test import TestCase
from django.urls import reverse
from .models import Book, Review
from django.contrib.auth import get_user_model


class BookTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.user = get_user_model().objects.create_user(
        username = 'testuser',
        email  = 'testuser@gmail.com',
        password = '1234',
        )

        cls.book = Book.objects.create(
            title = "Harry Potter",
            author = "J.K. Rowling",
            price = "10.99",
        )

        cls.review  = Review.objects.create(
            book=cls.book,
            author=cls.user,
            review="Great book",
        )

    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "Harry Potter")
        self.assertEqual(f"{self.book.author}", "J.K. Rowling")
        self.assertEqual(f"{self.book.price}", "10.99")     

    def test_book_list_view(self):
        response = self.client.get(reverse("books"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response,"books/books.html")

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response  =self.client.get("/books/12345")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, "Great book")
        self.assertTemplateUsed(response,"books/book_details.html")