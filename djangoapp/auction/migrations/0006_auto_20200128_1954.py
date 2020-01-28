# Generated by Django 3.0.1 on 2020-01-28 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_remove_offer_service_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='current_average_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price_percentage_change',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=4),
            preserve_default=False,
        ),
    ]