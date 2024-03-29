# Generated by Django 5.0.2 on 2024-03-06 12:27

from django.db import migrations, models
from django.utils import timezone

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('product_name', models.CharField(max_length=255)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='PriceListUpdateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(default=timezone.now))
            ],
        ),
    ]
