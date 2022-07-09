from django.contrib import admin
from .models import Services_table

# Register your models here.

@admin.register(Services_table)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']