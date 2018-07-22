from django.shortcuts import render
from django.core import serializers
from django.views import generic
from life.models import *

def index(request):
    num_items = Item.objects.all().count()
    num_deals = Deal.objects.all().count()
    return render(
        request,
        'life/index.html',
        context={'num_items':num_items,'num_deals':num_deals},
    )

class ItemListView(generic.ListView):
    model = Item


class ItemDetailView(generic.DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['deal_list'] = self.object.deals.all()
        return context

class DealListView(generic.ListView):
    model = Deal

class DealDetailView(generic.DetailView):
    model = Deal