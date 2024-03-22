from django.db import models
from django.utils import timezone

class PriceList(models.Model):
    code = models.CharField(max_length=255, default='')
    branch = models.CharField(max_length=255, default='')
    product_name = models.CharField(max_length=255, default='', blank=True)
    unit_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, blank=True)
    apply_unit_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, blank=True)
    delivery_lot = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, blank=True)
    pre_order_lot = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, blank=True)
    unit = models.CharField(max_length=255, default='', blank=True)
    packaging_style = models.CharField(max_length=255, default='', blank=True)
    supplier_code = models.CharField(max_length=255, default='', blank=True)
    supplier = models.CharField(max_length=255, default='', blank=True)
    delivery_code = models.CharField(max_length=255, default='', blank=True)
    delivery_location = models.CharField(max_length=255, default='', blank=True)
    applicable_location = models.CharField(max_length=255, default='', blank=True)
    note = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.code}-{self.branch} - {self.product_name}"

class PriceListUpdateHistory(models.Model):
    code = models.CharField(max_length=255, default='')
    branch = models.CharField(max_length=255, default='')
    product_name = models.CharField(max_length=255, default='', blank=True)
    unit_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, blank=True)
    apply_unit_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, blank=True)
    delivery_lot = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, blank=True)
    pre_order_lot = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, blank=True)
    unit = models.CharField(max_length=255, default='')
    packaging_style = models.CharField(max_length=255, default='')
    supplier_code = models.CharField(max_length=255, default='')
    supplier = models.CharField(max_length=255, default='')
    delivery_code = models.CharField(max_length=255, default='')
    delivery_location = models.CharField(max_length=255, default='')
    applicable_location = models.CharField(max_length=255, default='')
    note = models.TextField(default='')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.code} - {self.product_name}"
