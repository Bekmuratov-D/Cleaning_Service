from django.db import models

# Create your models here.


class Services_table(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(default='', null=False, blank=True)
    def __str__(self):                            # для вывода в током виде f'{self.name} - {self.rating}'
        return f'{self.name}'