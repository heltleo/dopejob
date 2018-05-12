from django.contrib import admin
from rental.models import Car
from rental.models import Booking
from rental.models import Contact
from rental.models import Account

# Register your models here.
class ContactFormAdmin(admin.ModelAdmin):
    class Meta:
        model = Contact


class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer', 'booking_start_date', 'booking_end_date', 'is_approved']
    list_filter = ['is_approved']
    search_fields = ['customer__username']
    list_editable = ['is_approved']

admin.site.register(Car)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Contact, ContactFormAdmin)
admin.site.register(Account)
