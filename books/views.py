from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book
from django.db.models import Q



class BookListView(LoginRequiredMixin, ListView):
    template_name = 'books/books.html'
    model = Book
    login_url = "account_login"
    
class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = "books/book_details.html"
    login_url = "account_login"
    permission_required = "books.special_status"
    queryset = Book.objects.all().prefetch_related("reviews__author")

    def get_permission_denied_message(self):
        return "Not allowed here!!!!"
    
class SearchListView(ListView):
    template_name = 'books/search.html'
    model = Book
    context_object_name = 'search'

    def get_queryset(self):
        query = self.request.GET.get("q") # pobiera wartość z nazwy input w forms z _base.html. GET to słownik
        searched_book = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        return searched_book
     
       