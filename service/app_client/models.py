from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(default='', null=False, blank=True)
    def __str__(self):                            # для вывода в током виде f'{self.name} - {self.rating}'
        return f'{self.name}'
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Service, self).save(*args, **kwargs)
    def get_url(self):
        return reverse('show_offer_services', args=[self.slug])


class Offers(models.Model):
    name_offer = models.CharField(max_length=300)
    description = models.TextField()
    slug = models.SlugField(default='', null=False, blank=True)
    service = models.ForeignKey(Service, on_delete=models.PROTECT, null=True, related_name='service')