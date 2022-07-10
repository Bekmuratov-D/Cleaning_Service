from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Services_table, Offers_table, Order_table
from .forms import OrderForm

# Create your views here.

def auth(request):
    return render(request, 'app/auth.html')

def service(request):
    services = Services_table.objects.all()
    return render(request, 'app/service.html', {
        'services' : services
    })

def offers(request, slug_service:str):
    slug_service = get_object_or_404(Services_table, slug=slug_service)
    offers = Offers_table.objects.all()
    return render(request, 'app/offers.html', {
        'slug_service' : slug_service,
        'offers' : offers
    })

def one_offer(request, slug_offer:str):
    offer = get_object_or_404(Offers_table, slug=slug_offer)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            order = Order_table(
                address=form.cleaned_data['address'],
                tel=form.cleaned_data['tel'],
                offer = get_object_or_404(Offers_table, slug=slug_offer)
            )
            order.save()
            return HttpResponseRedirect('#')
    else:
        form = OrderForm()
    return render(request, 'app/one_offer.html', context={
        'form': form,
        'offer' : offer
        })





