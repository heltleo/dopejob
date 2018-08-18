from django import forms

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.mail import send_mail

from accounts.forms import UserAdminCreationForm
from accounts.forms import UserAdminChangeForm

from accounts.models import User
from accounts.models import Message
from accounts.models import Faculty
from accounts.models import Campus
from accounts.models import Job
from accounts.models import Employee
from accounts.models import Student
from accounts.models import Enterprise
from accounts.models import Cursus

# Register your models here.
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('registration_number', 'email', 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('author', 'topic', 'content',)
        widgets = {
            'content': forms.Textarea(attrs={'disabled': True})
        }

class MessageFormAdmin(admin.ModelAdmin):
    list_display = ['author', 'topic', 'publication_date']
    search_fields = ['author', 'content']
    list_filter = ['topic']
    form = MessageForm


admin.site.register(User, UserAdmin)
admin.site.register(Faculty)
admin.site.register(Message, MessageFormAdmin)
admin.site.register(Campus)
admin.site.register(Job)
admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(Cursus)
admin.site.register(Enterprise)

# Unregister the Group Model
admin.site.unregister(Group)
