from datetime import datetime, timezone
from rest_framework import serializers
from .models import Book, Author


# The AuthorSerializer serializes the Author model and includes the related books
# using a nested BookSerializer. The BookSerializer validates that the publication year
# is not in the future.

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # def validate(self, request, obj):
    #     nowyear = timezone.now()
    #     publication_year = obj.Book.publication_year
    #     if nowyear > publication_year:
    #         return True
    #     else:
    #         raise serializers.validationError('erro data')
    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer(many = True, read_only = True)

    class Meta:
        model = Author
        fields = ['name', 'book']