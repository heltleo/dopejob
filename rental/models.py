import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Car(models.Model):
    BERLINE = 'BE'
    COUPE = 'CO'
    CABRIOLET = 'CA'
    ROADSTER = 'RA'
    KATKAT = 'KA'
    SUV = 'SU'
    CROSSOVER = 'CR'
    BREAK = 'BR'
    MONOSPACE = 'MO'
    CARS_MODEL_CHOICES = (
        (BERLINE, 'Berline'),
        (COUPE, 'Coupé'),
        (CABRIOLET, 'Cabriolet'),
        (ROADSTER, 'Roadster'),
        (KATKAT, '4X4'),
        (SUV, 'Suv'),
        (CROSSOVER, 'Crossover'),
        (BREAK, 'Break'),
        (MONOSPACE, 'Monospace'),
    )
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='car_images')
    description = models.TextField()
    daily_rent = models.IntegerField()
    is_available = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    localization = models.CharField(max_length=100, blank=True, null=True)
    car_models = models.CharField(
        max_length=2,
        choices=CARS_MODEL_CHOICES,
        default=BERLINE,
    )


    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('car-details', kwargs={'pk', self.pk})

    def was_published_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    def is_upperclass(self):
        return self.model in (self.BERLINE, self.CABRIOLET)

    def __str__(self):
        return 'Car {}'.format(self.name)


class Booking(models.Model):
    customer = models.ForeignKey(User, related_name='cars', on_delete=models.CASCADE)
    booking_start_date = models.DateTimeField()
    booking_end_date = models.DateTimeField()
    is_approved = models.BooleanField()

    def __str__(self):
        return 'Booking by {} on {}'.format(self.customer, self.booking_start_date)
