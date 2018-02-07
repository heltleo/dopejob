import hashlib

from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponse, Http404
from django.template import loader, RequestContext
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from rental.forms import ContactForm, PostCarForm, UserCreationForm, BookingCarForm
from rental.models import Car, Booking, Contact
from rental.filters import CarFilter

# Create your views here.
def index(request):
    latest_cars = Car.objects.order_by('-created')
    car_filter = CarFilter(request.GET, queryset=latest_cars)

    context = {
        'filter': car_filter,
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


class RegistrationFormView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/registration_form.html'

    def form_valid(self, form):
        user = User.objects.create_user(form.cleaned_data['username'],
                                        form.cleaned_data['email'],
                                        form.cleaned_data['password1'])
        user.is_active = True
        user.save()
        date = user.date_joined.replace(microsecond=0)
        key = hashlib.sha1((u'%s%s%s' % (settings.SECRET_KEY, user.email, date)
                            ).encode('utf-8')).hexdigest()

        subject = _(u'[%s] : Subscription') % settings.SITE_NAME

        mail = render_to_string('authentication/mails/registration_confirmation.html',
                                { 'titre': subject,
                                  'pseudo': user.username,
                                  'site': settings.SITE_NAME,
                                  'user_id': user.id,
                                  'user_key': key })

        msg = EmailMessage(subject, mail, '%(site)s <%(email)s>' % {
                'site': settings.SITE_NAME, 'email': settings.DEFAULT_FROM_EMAIL
                }, [user.email])

        msg.content_subtype = "html"
        msg.send()

        return redirect('rent_a_car')

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
