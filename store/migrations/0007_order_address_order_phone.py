# Generated by Django 4.0.1 on 2022-05-24 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_orders_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='0, blank=true', max_length=50),
        ),
    ]
