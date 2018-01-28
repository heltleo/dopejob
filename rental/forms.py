from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Contact, Car


class ContactForm(ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = ('name', 'email', 'topic', 'message',)


class PostCarForm(ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Car
        fields = ('name', 'image', 'description', 'daily_rent', 'localization', 'car_models',)


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
