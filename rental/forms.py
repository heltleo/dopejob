from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = ('name', 'email', 'topic', 'message',)
