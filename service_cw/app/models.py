from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Services_table(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(default='', null=False, blank=True)
    def __str__(self):                            # для вывода в током виде f'{self.name} - {self.rating}'
        return f'{self.name}'
    def get_url(self):
        return reverse ('offers', args=[self.slug])



class Company_table(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):                         
        return f'{self.name}'


class Offers_table(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(default=0)
    service = models.ForeignKey(Services_table, on_delete=models.PROTECT, null=True)
    company = models.ForeignKey(Company_table, on_delete=models.PROTECT, blank=True, null=True)
    
    def __str__(self):                         
        return f'{self.name} - {self.service} -{self.company} - {self.price}'

