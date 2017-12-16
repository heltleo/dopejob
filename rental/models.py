from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='car_images')
    description = models.TextField()
    daily_rent = models.IntegerField()
    is_available = models.BooleanField()

    def get_absolute_url(self):
        return reverse('car-details', kwargs={'pk', self.pk})

    def __str__(self):
        return self.name

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    booking_start_date = models.DateTimeField()
    booking_end_date = models.DateTimeField()
    is_approved = models.BooleanField()
