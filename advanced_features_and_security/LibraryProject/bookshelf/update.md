# Update the Book Instance

```python
book = Book.objects.get(id=<id>)
book.title = "Nineteen Eighty-Four"
book.save()
# Expected output: Title updated to Nineteen Eighty-Four
