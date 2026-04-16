from django.urls import path
from .views import get_books, get_book_detail

urlpatterns = [
    path('books/', get_books),
    path('books/<int:id>/', get_book_detail),
]