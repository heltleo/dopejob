from django import forms
from django.contrib.auth.models import User
from .models import Contact
from .models import Car
from .models import Booking
from django.contrib.admin import widgets

class ContactForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Please enter the message'}))

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'topic',
            'message',
        )


class PostCarForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.Textarea, help_text='Details of the vehicle.')

    class Meta:
        model = Car
        fields = (
            'name',
            'image',
            'description',
            'daily_rent',
            'localization',
            'car_models',
        )


class BookingCarForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = (
            'booking_start_date',
            'booking_end_date',
        )

    def __init__(self, *args, **kwargs):
        super(BookingCarForm, self).__init__(*args, **kwargs)
        self.fields['booking_start_date'].widget = widgets.AdminDateWidget()
        self.fields['booking_end_date'].widget = widgets.AdminDateWidget()
