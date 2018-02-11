from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils.translation import ugettext as _
from django.core.mail import EmailMessage
from rental.forms import ContactForm, PostCarForm, BookingCarForm
from rental.models import Car, Booking, Contact
from rental.filters import CarFilter

# Create your views here.
def index(request):
    latest_cars = Car.objects.all().filter(is_available=True)
    number_of_cars = len(latest_cars)
    car_filter = CarFilter(request.GET, queryset=latest_cars)


    context = {
        'filter': car_filter,
        'number_of_cars': number_of_cars,
        'selected': 'newest',
        # 'latest_cars': latest_cars
    }
    return render(request, 'rental/index.html', context)

def sort_by_oldest(request):
    oldest_cars = Car.objects.all().order_by('created').filter(is_available=True)
    number_of_cars = len(oldest_cars)
    car_filter = CarFilter(request.GET, queryset=oldest_cars)

    context = {
        'filter': car_filter,
        'number_of_cars': number_of_cars,
        'selected': 'oldest',
        # 'latest_cars': latest_cars
    }
    return render(request, 'rental/index.html', context)

def detail(request, id):
    car = get_object_or_404(Car, pk=id)
    form = BookingCarForm()

    if request.method == 'POST':
        form = BookingCarForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.is_approved = False
            car.is_available = False
            booking.save()
            return redirect('car-details', id=car.id)
        else:
            print(forms.errors)
    else:
        form = BookingCarForm(data=request.GET)

    #try:
        #car = Car.objects.get(pk=id)
    #except Car.DoesNotExist:
        #raise Http404('Car does not exist.')

    context = {
        'car': car,
        'form': form
    }
    return render(request, 'rental/detail.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            messages.add_message(
                request, messages.INFO, 'Your message has been sent. Thank you.'
            )
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


class PricingView(TemplateView):
    template_name='rental/pricing.html'


@login_required
def post_car_detail(request):
    form = PostCarForm()

    if request.method == 'POST':
        form = PostCarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('cars')
        else:
            print(form.errors)
    else:
        form = PostCarForm(data=request.GET)

    context = {'form':form}

    return render(request, 'rental/forms/rent_car.html', context)

@login_required
def settings(request):

    context = {
        'selected': 'account'
    }

    return render(request, 'dashboard/account_settings.html', context)

@login_required
def settings_payment(request):

    context = {
        'selected': 'payment'
    }

    return render(request, 'dashboard/payment_settings.html', context)
