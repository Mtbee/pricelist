from django.db import models
from django.utils import timezone

class PriceList(models.Model):
    code = models.CharField(max_length=255, unique=True)
    product_name = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.code} - {self.product_name}"

class PriceListUpdateHistory(models.Model):
    code = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.code} - {self.product_name}"
