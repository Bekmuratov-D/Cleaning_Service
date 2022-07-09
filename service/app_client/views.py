from django.shortcuts import render, get_object_or_404
from .models import Service, Offers
# Create your views here.


def auth_page(request):
    return render(request, 'app_client/auth_page.html')

def show_all_services(request):
    services = Service.objects.all()
    for service in services:
        service.save()
    for service in services:
        service.save()
    return render(request, 'app_client/service_page.html', {
        'services': services,
    })

def show_offer_services(request, slug_service:str):
    offers = get_object_or_404(Service, slug=slug_service)
    return render(request, 'app_client/show_offer_servises.html', {
        'offers': offers
    })