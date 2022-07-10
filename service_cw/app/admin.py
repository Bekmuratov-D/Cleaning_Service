from django.contrib import admin
from .models import Services_table, Offers_table, Company_table, Order_table

# Register your models here.

@admin.register(Services_table)
class Services_tableAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name', )} 



@admin.register(Offers_table)
class Offers_tableAdmin(admin.ModelAdmin):
    list_display = ['name', 'service', 'price', 'company']
    prepopulated_fields = {'slug' : ('name', 'company' , )} 

@admin.register(Company_table)
class Company_tableAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug' : ('name', )} 

@admin.register(Order_table)
class Order_tableAdmin(admin.ModelAdmin):
    list_display = ['address', 'tel', 'offer']