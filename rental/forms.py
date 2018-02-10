from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
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


class BookingCarForm(ModelForm):
    booking_start_date = forms.DateTimeField(required=True, help_text='debut rent')
    booking_end_date = forms.DateTimeField(required=True, help_text='end rent')

    class Meta:
        model = Booking
        fields = ('booking_start_date', 'booking_end_date',)
