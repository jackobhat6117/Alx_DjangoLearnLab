from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # handle editing logic
        pass
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')



def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books})

from django.http import HttpResponse

def my_view(request):
    response = HttpResponse("Content")
    response['Content-Security-Policy'] = "default-src 'self'; script-src 'self' https://trustedscripts.com"
    return response

from django.shortcuts import render
from .forms import ExampleForm

# Example view using the ExampleForm
def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Add your logic here (e.g., saving data or sending an email)
            return render(request, 'bookshelf/success.html', {'name': name})
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/example_form.html', {'form': form})
