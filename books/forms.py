from django import forms
from .widgets import MyClearableFileInput
from .models import Book, Genre


class BookForm(forms.ModelForm):
    """ Book instance Form"""
    class Meta:
        model = Book
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=MyClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        view_genre = [(g.id, g.get_view_genre()) for g in genres]
        self.fields['genre'].choices = view_genre