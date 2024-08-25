```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Expected output: Book instance created with id=<id>
# Retrieve the Book Instance

```python
book = Book.objects.get(id=<id>)
print(book.title, book.author, book.publication_year)
# Expected output: 1984 George Orwell 1949
# Update the Book Instance

```python
book = Book.objects.get(id=<id>)
book.title = "Nineteen Eighty-Four"
book.save()
# Expected output: Title updated to Nineteen Eighty-Four
# Delete the Book Instance

```python
book = Book.objects.get(id=<id>)
book.delete()
# Expected output: Book instance deleted
