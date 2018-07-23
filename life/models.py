from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


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

    def get_shopping_list_url(self):
        return reverse('shopping-list-add', args=[str(self.id)])

    @classmethod
    def create(cls, name, price):
        item = cls(name=name, price=price)
        return item

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shopping_list = models.ManyToManyField('Item', related_name='shoppinglist_requests_created')
    history = models.ManyToManyField('Item', related_name='history_requests_created')
