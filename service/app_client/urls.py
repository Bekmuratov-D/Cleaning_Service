from django.urls import path, include
from .views import auth_page, show_all_services, show_offer_services

urlpatterns = [
    path('', auth_page),
    path('servise/<slug:slug_service>', show_offer_services, name='show_offer_services'),
    path('servise/', show_all_services),

]
