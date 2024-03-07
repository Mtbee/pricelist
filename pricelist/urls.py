# pricelist/urls.py

from django.urls import path
from .views import price_list, request_update_price_list, update_history_list, update_price_list

urlpatterns = [
    path('price_list/', price_list, name='price_list'),
    path('request_update_price_list/', request_update_price_list, name='request_update_price_list'),
    path('update_history_list/', update_history_list, name='update_history_list'),
    path('update_price_list/', update_price_list, name='update_price_list'),
]
