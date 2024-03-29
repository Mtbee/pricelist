# Generated by Django 5.0.2 on 2024-03-22 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricelist', '0002_pricelist_applicable_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricelist',
            name='applicable_location',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='apply_unit_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='delivery_code',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='delivery_location',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='delivery_lot',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='note',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='packaging_style',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='pre_order_lot',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='product_name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='supplier',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='supplier_code',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='unit',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='unit_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='pricelistupdatehistory',
            name='apply_unit_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='pricelistupdatehistory',
            name='delivery_lot',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='pricelistupdatehistory',
            name='pre_order_lot',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='pricelistupdatehistory',
            name='product_name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='pricelistupdatehistory',
            name='unit_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20),
        ),
    ]
