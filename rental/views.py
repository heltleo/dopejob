from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from rental.forms import ContactForm
from rental.models import Car, Booking, Contact

# Create your views here.
def index(request):
    latest_cars = Car.objects.order_by('-created')[:5]
    context = {
        'latest_cars': latest_cars,
    }
    return render(request, 'rental/index.html', context)

def detail(request, id):
    car = get_object_or_404(Car, pk=id)
    #try:
        #car = Car.objects.get(pk=id)
    #except Car.DoesNotExist:
        #raise Http404('Car does not exist.')
    return render(request, 'rental/detail.html', {'car': car})

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
