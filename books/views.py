from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
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
