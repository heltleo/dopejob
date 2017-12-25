from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from rental.models import Car, Booking

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
