
from django.urls import path
from .views import auth, service

urlpatterns = [
    path('', auth),
    path('service', service)
]