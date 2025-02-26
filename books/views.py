from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book



class BookListView(LoginRequiredMixin, ListView):
    template_name = 'books/books.html'
    model = Book
    login_url = "account_login"
    
    

class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = "books/book_details.html"
    login_url = "account_login"
    permission_required = "books.special_status"
    permission_denied_message ="asdasdasdasdas"

    def get_permission_denied_message(self):
        return "Not allowed here!!!!"