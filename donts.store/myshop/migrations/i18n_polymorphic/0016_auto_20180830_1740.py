# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-30 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0015_scootermodel_battery_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scootervariant',
            name='battery_capacity',
            field=models.PositiveIntegerField(help_text='Battery capacity in mAh', verbose_name='Battery capacity'),
        ),
    ]
