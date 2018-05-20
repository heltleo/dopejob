from django.contrib import admin
from django.core.mail import send_mail
from rental.models import Car
from rental.models import Booking
from rental.models import Contact
from rental.models import Account

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'daily_rent', 'is_available', 'owner', 'localization', 'created']
    list_filter = ['is_available']
    search_fields = ['localization', 'owner__username']
    list_editable = ['is_available',]

    class Meta:
        model = Car

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'topic', 'timestamp']
    search_fields = ['name']
    list_filter = ['topic']

    class Meta:
        model = Contact


class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer', 'car', 'booking_start_date', 'booking_end_date', 'is_approved']
    list_filter = ['is_approved']
    search_fields = ['customer__username']
    list_editable = ['is_approved']

    actions = ['email_customers']

    def email_customers(self, request, queryset):
        for booking in queryset:
            if booking.is_approved:
                email_body = """Dear, {}, We are pleased to inform you that your booking has been approved. Thanks""".format(booking.customer.username)
            else:
                email_body = """Dear {}, Unfortunatly we do not have the capacity right now to accept your booking. Thanks""".format(booking.customer.username)

            print(email_body)

            send_mail(
                'Your Booking on Activcar',
                email_body,
                'no-reply@activcar.com',
                [booking.customer.email],
                fail_silently=False,
            )

        self.message_user(request, 'Emails were send successfully')
    email_customers.short_description = 'Send email about booking status to customers'

admin.site.register(Car, CarAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Contact, ContactFormAdmin)
admin.site.register(Account)
