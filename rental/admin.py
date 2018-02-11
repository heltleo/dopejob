from django.contrib import admin
from rental.models import Car, Booking, Contact, Account

# Register your models here.
class ContactFormAdmin(admin.ModelAdmin):
    class Meta:
        model = Contact

admin.site.register(Car)
admin.site.register(Booking)
admin.site.register(Contact, ContactFormAdmin)
admin.site.register(Account)
