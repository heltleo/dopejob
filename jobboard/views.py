from django.shortcuts import render, redirect
from accounts.models import User
from accounts.models import Student
from accounts.models import Employee

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
