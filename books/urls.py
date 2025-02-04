from django.urls import path
from .views import BookTemplateView
from .views import BookDetailView


urlpatterns = [
    path('book_detail/<uuid:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('', BookTemplateView.as_view(), name='books'),

]