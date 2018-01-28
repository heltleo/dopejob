from rental.models import Car
import django_filters

class CarFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = ['name', 'daily_rent', 'localization', 'car_models',]
