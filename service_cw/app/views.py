from django.shortcuts import render
from .models import Services_table, Offers_table

# Create your views here.

def auth(request):
    return render(request, 'app/auth.html')

def service(request):
    services = Services_table.objects.all()
    return render(request, 'app/service.html', {
        'services' : services
    })

def offers(request):
    offers = Offers_table.objects.all()
    return render(request, 'app/offers.html', {
        'offers' : offers
    })