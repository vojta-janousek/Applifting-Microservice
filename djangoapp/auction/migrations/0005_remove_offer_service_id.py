# Generated by Django 3.0.1 on 2020-01-28 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_auto_20200127_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='service_id',
        ),
    ]
