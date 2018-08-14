from django import forms
from rental.models import Car
import django_filters

class CarFilter(django_filters.FilterSet):
    localization = django_filters.CharFilter(lookup_expr='icontains', label='', widget=forms.TextInput(attrs={'placeholder': 'Enter you city'}))
    car_models = django_filters.MultipleChoiceFilter(choices=Car.CARS_MODEL_CHOICES, widget=forms.CheckboxSelectMultiple, label='Car types')

    class Meta:
        model = Car
        fields = ['localization', 'car_models',]
