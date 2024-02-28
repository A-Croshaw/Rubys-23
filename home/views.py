from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from newsletter.forms import SubscribersForm
from newsletter.models import Subscribers
from books.models import Book

def index(request):
    """ A view to return the home page """
    books = Book.objects.all()

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "No Books with that criteria")
            return redirect(reverse('home'))

        queries = Q(title__icontains=query) | Q(description__icontains=query)
        books = books.filter(queries)
        context = {
        'books': books,
        'search_term': query,
        }
        return render(request, 'books/books.html', context)

    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you, your Subscription is successful.')
            return render(request, 'home/index.html')
    else:
        form = SubscribersForm()

    context = {
        'form': form,
        'books': books,
    }

    return render(request, 'home/index.html', context)
