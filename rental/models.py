import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='car_images')
    description = models.TextField()
    daily_rent = models.IntegerField()
    is_available = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('car-details', kwargs={'pk', self.pk})

    def was_published_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return 'Car {}'.format(self.name)


class Booking(models.Model):
    customer = models.ForeignKey(User, related_name='cars', on_delete=models.CASCADE)
    booking_start_date = models.DateTimeField()
    booking_end_date = models.DateTimeField()
    is_approved = models.BooleanField()

    def __str__(self):
        return 'Booking by {} on {}'.format(self.customer, self.booking_start_date)
