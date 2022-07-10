
from django.urls import path
from .views import auth, service, offers, one_offer, all_orders

urlpatterns = [
    path('', auth),
    path('service', service),
    path('service/<slug:slug_service>', offers, name='offers'),
    path('service/offer/<slug:slug_offer>', one_offer , name='one_offer'),
    path('orders', all_orders),
]