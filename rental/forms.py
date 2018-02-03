from django import forms
from django.forms import ModelForm
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Contact, Car, Booking


class ContactForm(ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = ('name', 'email', 'topic', 'message',)


class PostCarForm(ModelForm):
    image = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.Textarea, help_text='Details of the vehicle.')

    class Meta:
        model = Car
        fields = ('name', 'image', 'description', 'daily_rent', 'localization', 'car_models',)


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class BookingCarForm(ModelForm):
    booking_start_date = forms.DateTimeField(required=True, help_text='debut rent')
    booking_end_date = forms.DateTimeField(required=True, help_text='end rent')

    class Meta:
        model = Booking
        fields = ('booking_start_date', 'booking_end_date',)
