
from django.urls import path
from .views import auth, service, offers

urlpatterns = [
    path('', auth),
    path('service', service),
    path('service/offers', offers),
]