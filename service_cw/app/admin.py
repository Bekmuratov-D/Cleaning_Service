from django.contrib import admin
from .models import Services_table, Offers_table, Company_table, Order_table
from django.contrib.admin import AdminSite
from django.db.models import QuerySet

# Register your models here.


@admin.register(Services_table)
class Services_tableAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug' : ('name', )} 
    list_editable = ['name', 'slug']



@admin.register(Offers_table)
class Offers_tableAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'service', 'price', 'company']
    prepopulated_fields = {'slug' : ('name', 'company' , )} 
    list_editable = ['name','service', 'price', 'company']
    ordering = ['-price', 'name']

@admin.register(Company_table)
class Company_tableAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {'slug' : ('name', )} 
    list_editable = ['name']

@admin.register(Order_table)
class Order_tableAdmin(admin.ModelAdmin):
    list_display = ['id', 'address', 'tel', 'offer']
    list_editable = ['address', 'tel', 'offer']


# class PriceFilter(admin.SimpleListFilter):
#     title = 'Фильтр по цене'
#     parameter_name = 'price' 

#     def lookups(self, request, model_admin):
#         return [
#             ('<600', 'Низкая цена'),
#             ('от 600 до 1200', 'Хорошая цена'),
#             ('от 1200 до 2000', 'Высокая цена'),
#             ('>=80', 'без отценок'),
#         ]

#     def queryset(self, request, queryset):
#         if self.value() == '<40':
#             return queryset.filter(rating__lt=40)
#         if self.value() == 'от 40 до 59':
#             return queryset.filter(rating__gte=40).filter(rating__lt=60)
#         if self.value() == 'от 60 до 79':
#             return queryset.filter(rating__gte=60).filter(rating__lt=80)
#         if self.value() == '>=80':
#             return queryset.filter(rating__gt=80)
#         return queryset