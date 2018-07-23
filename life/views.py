from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.views import generic
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .forms import *
from life.models import *


def index(request):
    num_items = Item.objects.all().count()
    num_deals = Deal.objects.all().count()
    return render(
        request,
        'life/index.html',
        context={'num_items':num_items,'num_deals':num_deals},
    )   

@login_required
def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            item = Item.create(form.cleaned_data['name'], form.cleaned_data['price'])
            item.save()
            
            u = request.user.profile
            u.history.add(item)
            u.save()
            return HttpResponseRedirect('/')
    else:
        form = AddItemForm()

    return render(request, 'life/add_item.html', {'form': form})


class ShoppingListView(LoginRequiredMixin, generic.ListView):
    model = Item

    def get_queryset(self):
        u = self.request.user.profile 
        if u.shopping_list:
            return u.shopping_list.all()
        return None

class ItemListView(LoginRequiredMixin, generic.ListView):
    model = Item

    def get_queryset(self):
        u = self.request.user.profile 
        if u.history:
            return u.history.all()
        return None


class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['deal_list'] = self.object.deals.all()
        
        item = context['item'].name

        u = self.request.user.profile
        shopping_list = u.shopping_list.all()
        
        items = []
        for obj in shopping_list:
            items.append(obj.name)

        if item in items:
            context['addable'] = False
        else:
            context['addable'] = True

        return context

class ShoppingListAddView(LoginRequiredMixin, generic.DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super(ShoppingListAddView, self).get_context_data(**kwargs)
        
        pk = self.kwargs['pk']
        item = context['item']
        u = self.request.user.profile
        u.shopping_list.add(item)
        u.save()

        return context

class DealListView(LoginRequiredMixin, generic.ListView):
    model = Deal

class DealDetailView(LoginRequiredMixin, generic.DetailView):
    model = Deal
    


