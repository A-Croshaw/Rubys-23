from django import forms
from .widgets import MyClearableFileInput
from .models import Book, Genre


class BookForm(forms.ModelForm):
    """ Book instance Form"""
    class Meta:
        model = Book
        fields = (
            'genre', 'category', 'sku', 'ISBN',
            'author', 'title', 'link', 'pages',
            'first_published', 'this_publication_date',
            'condition', 'description', 'language',
            'price', 'rating', 'image',)

    image = forms.ImageField(
        label='Image', required=False,
        widget=MyClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes,
        set autofocus on first field.
        And adds genre items to dropdown
        """
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        view_genre = [(g.id, g.get_view_genre()) for g in genres]
        self.fields['genre'].choices = view_genre
        self.fields['title'].widget.attrs['autofocus'] = True

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'book-form'
