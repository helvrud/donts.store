# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-30 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0019_remove_scootermodel_battery_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='scootermodel',
            name='battery_capacity',
            field=models.DecimalField(decimal_places=1, help_text='Battery capacity in Ah', max_digits=3, null=True, verbose_name='Battery capacity'),
        ),
        migrations.AlterField(
            model_name='scootervariant',
            name='battery_capacity',
            field=models.DecimalField(decimal_places=1, help_text='Battery capacity in Ah', max_digits=3, verbose_name='Battery capacity'),
        ),
    ]
