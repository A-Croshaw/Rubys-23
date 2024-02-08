from django import forms
from . models import Subscribers, Newsletters


class SubscribersForm(forms.ModelForm):
    
    class Meta:
        model = Subscribers
        fields = ['email',]


class NewslettersForm(forms.ModelForm):
    class Meta:
        model = Newsletters
        fields = '__all__'