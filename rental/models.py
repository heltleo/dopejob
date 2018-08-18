import datetime
import uuid
from decimal import Decimal
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

# class Car(models.Model):
#     BERLINE = 'BE'
#     COUPE = 'CO'
#     CABRIOLET = 'CA'
#     ROADSTER = 'RA'
#     KATKAT = 'KA'
#     SUV = 'SU'
#     CROSSOVER = 'CR'
#     BREAK = 'BR'
#     MONOSPACE = 'MO'
#     CARS_MODEL_CHOICES = (
#         (BERLINE, 'Berline'),
#         (COUPE, 'Coupé'),
#         (CABRIOLET, 'Cabriolet'),
#         (ROADSTER, 'Roadster'),
#         (KATKAT, '4X4'),
#         (SUV, 'Suv'),
#         (CROSSOVER, 'Crossover'),
#         (BREAK, 'Break'),
#         (MONOSPACE, 'Monospace'),
#     )
#     name = models.CharField(max_length=100)
#
#     description = models.TextField()
#     daily_rent = models.FloatField()
#     is_available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     localization = models.CharField(max_length=100, blank=True, null=True)
#     owner = models.ForeignKey(User, on_delete=models.PROTECT)
#     car_models = models.CharField(
#         max_length=2,
#         choices=CARS_MODEL_CHOICES,
#         default=BERLINE,
#     )
#
#
#     class Meta:
#         ordering = ('-created',)
#
#
#     def get_absolute_url(self):
#         return reverse('car-details', kwargs={'pk', self.pk})
#
#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.created <= now
#
#     def is_upperclass(self):
#         return self.model in (self.BERLINE, self.CABRIOLET)
#
#     def __str__(self):
#         return 'Car {}'.format(self.name)
