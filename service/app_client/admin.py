from django.contrib import admin
from .models import Service, Offers
# Register your models here.

@admin.register(Service)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

@admin.register(Offers)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name_offer', 'description', 'service']
    prepopulated_fields = {'slug': ('name_offer', )}