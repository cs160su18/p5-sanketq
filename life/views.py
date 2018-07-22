from django.shortcuts import render
from django.core import serializers
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from life.models import *

def index(request):
    num_items = Item.objects.all().count()
    num_deals = Deal.objects.all().count()
    return render(
        request,
        'life/index.html',
        context={'num_items':num_items,'num_deals':num_deals},
    )

class ShoppingListView(LoginRequiredMixin, generic.ListView):
    model = Item

    def get_queryset(self):
        u = self.request.user
        return u.shopping_list.items.all()

class ItemListView(LoginRequiredMixin, generic.ListView):
    model = Item

    def get_queryset(self):
        u = self.request.user
        if u.history:
            return u.history.items.all()
        return Item.objects.all()

class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['deal_list'] = self.object.deals.all()
        return context

class DealListView(LoginRequiredMixin, generic.ListView):
    model = Deal

class DealDetailView(LoginRequiredMixin, generic.DetailView):
    model = Deal