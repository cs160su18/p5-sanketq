from django.db import models
from django.urls import reverse

class Deal(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    barcode_info = models.CharField(max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    
    
   
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('deal-detail', args=[str(self.id)])


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=6)
    deals = models.ManyToManyField('Deal')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item-detail', args=[str(self.id)])