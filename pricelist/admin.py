from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PriceList, PriceListUpdateHistory

admin.site.register(PriceList)
admin.site.register(PriceListUpdateHistory)