from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "Harry Potter",
            author = "J.K. Rowling",
            price = "10.99",

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
        self.assertTemplateUsed(response,"books/book_details.html")