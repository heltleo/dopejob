from django.contrib import admin

from accounts.models import User
from accounts.models import Message
from accounts.models import Faculty
from accounts.models import Campus
from accounts.models import Job
from accounts.models import Employee
from accounts.models import Student
from accounts.models import Cursus

# Register your models here.

admin.site.register(User)
admin.site.register(Faculty)
admin.site.register(Message)
admin.site.register(Campus)
admin.site.register(Job)
admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(Cursus)
