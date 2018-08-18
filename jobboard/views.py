from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.utils.translation import ugettext as _
from django.core.mail import EmailMessage

from accounts.models import User
from accounts.models import Student
from accounts.models import Employee

from jobboard.models import Annonce

from jobboard.filters import AnnonceFilter

# Create your views here.
def index(request):
    latest_annonces = Annonce.objects.all().filter(is_available=True)
    number_of_annonces = len(latest_annonces)
    annonce_filter = AnnonceFilter(request.GET, queryset=latest_annonces)

    return render(request, 'index.html', {
        'filter': annonce_filter,
        'annonce_filter': annonce_filter,
        'number_of_annonces': number_of_annonces,
    })
