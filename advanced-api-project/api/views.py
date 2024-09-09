from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# ListView: Retrieve all books and CreateView: Add a new book



class BookListView(generics.ListCreateAPIView):
    """
    Handles listing all books and creating new ones.
    Only authenticated users can create books, while unauthenticated users can view them.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        # Custom logic during book creation (if needed)
        serializer.save()

# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# UpdateView: Modify an existing book
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        book_id = request.data.get('id')
        book = self.get_object()
        if book_id is None or book_id != book.pk:
            return Response({'error': 'Invalid book ID'}, status=status.HTTP_400_BAD_REQUEST)
        return super().put(request, *args, **kwargs)


# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        book_id = request.data.get('id')
        book = self.get_object()
        if book_id is None or book_id != book.pk:
            return Response({'error': 'Invalid book ID'}, status=status.HTTP_400_BAD_REQUEST)
        return super().delete(request, *args, **kwargs)
