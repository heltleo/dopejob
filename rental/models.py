import datetime
import uuid
from decimal import Decimal
from django.db import models
from django.utils import timezone
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
    image = models.ImageField(upload_to='car_images/%Y/%m/%d/', blank=True)
    description = models.TextField()
    daily_rent = models.FloatField()
    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    localization = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    car_models = models.CharField(
        max_length=2,
        choices=CARS_MODEL_CHOICES,
        default=BERLINE,
    )


    class Meta:
        ordering = ('-created',)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def get_absolute_url(self):
        return reverse('car-details', kwargs={'pk', self.pk})

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created <= now

    def is_upperclass(self):
        return self.model in (self.BERLINE, self.CABRIOLET)

    def __str__(self):
        return 'Car {}'.format(self.name)


class Booking(models.Model):
    customer = models.ForeignKey(User, related_name='cars', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, related_name='cars_booked', on_delete=models.CASCADE, blank=True, null=True)
    booking_start_date = models.DateTimeField()
    booking_end_date = models.DateTimeField()
    is_approved = models.BooleanField()

    def __str__(self):
        return '{} Booking by {} on {} to {}'.format(self.car, self.customer, self.booking_start_date, self.booking_end_date)


class Contact(models.Model):
    GENERAL = 'GE'
    PAYMENT = 'PA'
    CAREERS = 'CA'
    TECHNICAL = 'TE'
    TOPIC_CHOICES = (
        (GENERAL,'General informations'),
        (PAYMENT, 'Payment'),
        (CAREERS, 'Careers'),
        (TECHNICAL, 'Technical support'),
    )
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=250)
    topic = models.CharField(
        max_length=2,
        choices=TOPIC_CHOICES,
        default=GENERAL,
    )
    message = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('-timestamp',)


class Account(models.Model):
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    user = models.ForeignKey(User, related_name='account', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    balance = models.PositiveIntegerField(verbose_name='Current balance', default=0)

    def __str__(self):
        return 'Customer {} have {} €'.format(self.user, self.balance)
