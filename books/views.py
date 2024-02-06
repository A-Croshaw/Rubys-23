from django.contrib.auth.decorators import (
    login_required, permission_required)
from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Book, Genre
from .forms import BookForm

def all_books(request):
    """
    A view to render all books with sorting and searching
    """
    books = Book.objects.all()
    genres = None
    query = None
    sort = None
    dir = None

    if request.GET:

        if 'sort' in request.GET:
            sorting = request.GET['sort']
            sort = sorting
            if sorting == 'title':
                sorting = 'lower_title'
                books = books.annotate(lower_title=Lower('title'))
            if sorting == 'genre':
                sorting = 'genre__genre'
            if 'dir' in request.GET:
                dir = request.GET['dir']
                if dir == 'desc':
                    sorting = f'-{sorting}'
            books = books.order_by(sorting)

        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            books = books.filter(genre__genre__in=genres)
            genres = Genre.objects.filter(genre__in=genres)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No Books with that criteria")
                return redirect(reverse('books'))

            queries = Q(title__icontains=query) | Q(description__icontains=query)
            books = books.filter(queries)

    sorted = f'{sort}_{dir}'
    context = {
        'books': books,
        'search_term': query,
        'sorted_genres': genres,
        'sorted': sorted,
    }

    return render(request, 'books/books.html', context)


def book_view(request, book_id):
    """ View to see full book """

    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book,
    }

    return render(request, 'books/book_view.html', context)


@login_required
@permission_required("books.add_book", raise_exception=True)
def add_book(request):
    """ Adding books to the store admin users only """
    if not request.user.is_superuser:
        messages.error(request, 'Admin users can only add books.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'{book.title} was successfully added')
            return redirect(reverse('book_view', args=[book.id]))
        else:
            messages.error(request,
                           f'failed to add {book.title}.'
                           'Please ensure the details are correct and'
                           'all fields that are required are entered.'
                           )
    else:
        form = BookForm()

    template = 'books/add_book.html'
    context = {
        'form': form,
    }


    return render(request, template, context)

@login_required
@permission_required("books.edit_book", raise_exception=True)
def edit_book(request, book_id):
    """ Edit a book in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Admin users only can edit books.')
        return redirect(reverse('home'))

    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f'{book.title} was successfully updated!')
            return redirect(reverse('book_view', args=[book.id]))
        else:
            messages.error(request,
                            f'Updating {book.title} failed. Please ensure the details are valid.')
    else:
        form = BookForm(instance=book)
        messages.info(request, f'Editing: {book.title}')

    template = 'books/edit_book.html'
    context = {
        'form': form,
        'book': book,
    }

    return render(request, template, context)


@login_required
@permission_required("books.book_delete", raise_exception=True)
def book_delete(request, book_id):
    """ Delete Book from Store """
    if not request.user.is_superuser:
        messages.error(request, 'Admin users can only delete books.')
        return redirect(reverse('home'))

    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        book.delete()
        messages.success(request, f'{book.title} has been delete successfully!')
        return redirect(reverse('books'))

    context = {
        'book':book,
    }
    return render(request, "books/book_delete.html", context)

