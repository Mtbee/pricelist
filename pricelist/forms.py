# pricelist/forms.py

from django import forms
from .models import PriceListUpdateHistory

class PriceListUpdateForm(forms.ModelForm):
    class Meta:
        model = PriceListUpdateHistory
        fields = ['code', 'product_name', 'unit_price']