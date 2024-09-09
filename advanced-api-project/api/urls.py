from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # /books/ for list view
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # /books/<id>/ for detail view
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # /books/create/ for creating new book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),  # /books/<id>/update/ for updating book
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),  # /books/<id>/delete/ for deleting book
]
