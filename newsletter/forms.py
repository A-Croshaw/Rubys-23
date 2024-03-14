from django import forms
from . models import Subscribers, Newsletters


class SubscribersForm(forms.ModelForm):

    class Meta:
        model = Subscribers
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        """
        Add class, remove auto-generated
        labels and set autofocus on email field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'Email',
        }

        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'newsletter-form'
            self.fields[field].label = False


class NewslettersForm(forms.ModelForm):
    class Meta:
        model = Newsletters
        fields = ('title', 'message',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'message': 'Message',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'newsletter-form'
            self.fields[field].label = False
