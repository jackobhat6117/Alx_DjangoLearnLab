from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

# The AuthorSerializer serializes the Author model and includes the related books
# using a nested BookSerializer. The BookSerializer validates that the publication year
# is not in the future.


# BookSerializer to serialize all fields of the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation to ensure the publication year is not in the future
    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value

# AuthorSerializer to include the name and a nested BookSerializer
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer for books related to the author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
