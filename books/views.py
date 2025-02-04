from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book

class BookTemplateView(ListView):
    template_name = 'books/books.html'
    model = Book


class BookDetailView(DetailView):
    template_name = "books/book_details.html"
    model = Book