from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

class BookSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search books...',
            'class': 'form-control'
        }),
        required=True
    )
