# Delete the Book Instance

```python
from bookshelf.models import Book

book = Book.objects.get(id=<id>)
book.delete()
# Expected output: Book instance deleted
