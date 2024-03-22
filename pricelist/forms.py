# pricelist/forms.py

from django import forms
from .models import PriceList

class PriceListUpdateForm(forms.ModelForm):
    class Meta:
        model = PriceList
        fields = '__all__'