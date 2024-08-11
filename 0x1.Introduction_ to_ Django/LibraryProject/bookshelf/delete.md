# Delete the Book Instance

```python
book = Book.objects.get(id=<id>)
book.delete()
# Expected output: Book instance deleted
