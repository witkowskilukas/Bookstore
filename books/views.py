from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from .models import Book
from .forms import ReviewModelForm
from django.db.models import Q
from django.urls import reverse_lazy



class BookListView(LoginRequiredMixin, ListView):
    template_name = 'books/books.html'
    model = Book
    login_url = "account_login"
    ordering = ['title']
    
class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "books/book_details.html"
    login_url = "account_login"
    queryset = Book.objects.all().prefetch_related("reviews__author")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewModelForm()
        context['review'] = self.object.reviews.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewModelForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = self.object
            review.author = request.user
            review.save()
            return redirect('book_detail', pk=self.object.pk)
        return self.get(request, *args, **kwargs)
    
class SearchListView(LoginRequiredMixin, ListView):
    template_name = 'books/search.html'
    model = Book
    context_object_name = 'search'

    def get_queryset(self):
        query = self.request.GET.get("q") # pobiera wartość z nazwy input w forms z _base.html. GET to słownik
        searched_book = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        return searched_book
     
       