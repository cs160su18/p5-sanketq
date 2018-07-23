from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class AddItemForm(forms.Form):
    name = forms.CharField(label="Enter the item's name.", max_length=200)
    price = forms.DecimalField(label="Enter the item's price.")