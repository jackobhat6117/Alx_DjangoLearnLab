# Retrieve the Book Instance

```python
book = Book.objects.get(id=<id>)
print(book.title, book.author, book.publication_year)
# Expected output: 1984 George Orwell 1949
