from django.contrib import admin
from .models import Book, Genre


class BookAdmin(admin.ModelAdmin):
    """
    Creates Admin For The Books
    """
    fieldsets = []

    ordering = ('sku',)
    list_display = (
        'sku',
        'ISBN',
        'author',
        'title',
        'pages',
        'category',
        'genre',
        'this_publication_date',
        'condition',
        'language',
        'price',
        'rating',
    )


class GenreAdmin(admin.ModelAdmin):
    """
    Creates Admin For The Genres
    """
    fieldsets = []
    list_display = (
        'view_genre',
        'genre',
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
