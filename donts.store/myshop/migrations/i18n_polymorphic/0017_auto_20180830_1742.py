# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-30 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0016_auto_20180830_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scootermodel',
            name='battery_capacity',
            field=models.DecimalField(decimal_places=1, help_text='Battery capacity in mAh', max_digits=5, verbose_name='Capacity'),
        ),
        migrations.AlterField(
            model_name='scootervariant',
            name='battery_capacity',
            field=models.DecimalField(decimal_places=1, help_text='Battery capacity in mAh', max_digits=5, verbose_name='Battery capacity'),
        ),
    ]
