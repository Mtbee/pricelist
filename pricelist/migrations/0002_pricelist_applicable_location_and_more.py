# Generated by Django 5.0.2 on 2024-03-14 09:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricelist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricelist',
            name='applicable_location',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pricelist',
            name='apply_unit_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='pricelist',
            name='branch',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pricelist',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='pricelist',
            name='delivery_code',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pricelist',
            name='delivery_location',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pricelist',
            name='delivery_lot',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='pricelist',
            name='note',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='pricelist',
            name='packaging_style',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pricelist',
            name='pre_order_lot',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='pricelist',
            name='supplier',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pricelist',
            name='supplier_code',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pricelist',
            name='unit',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pricelistupdatehistory',
            name='applicable_location',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pricelistupdatehistory',
            name='apply_unit_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='pricelistupdatehistory',
            name='branch',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pricelistupdatehistory',
            name='delivery_code',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pricelistupdatehistory',
            name='delivery_location',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pricelistupdatehistory',
            name='delivery_lot',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='pricelistupdatehistory',
            name='note',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='pricelistupdatehistory',
            name='packaging_style',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pricelistupdatehistory',
            name='pre_order_lot',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='pricelistupdatehistory',
            name='supplier',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pricelistupdatehistory',
            name='supplier_code',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pricelistupdatehistory',
            name='unit',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='code',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='product_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='pricelistupdatehistory',
            name='code',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='pricelistupdatehistory',
            name='product_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='pricelistupdatehistory',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
    ]
