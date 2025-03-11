from django.urls import path
from .views import BookListView
from .views import BookDetailView
from .views import SearchListView

urlpatterns = [
    path('search/', SearchListView.as_view(), name='search'),
    path('book_detail/<uuid:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('', BookListView.as_view(), name='books'),

]