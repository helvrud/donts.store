# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-31 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import djangocms_text_ckeditor.fields
import shop.money.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0022_auto_20180831_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScooterModel',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myshop.Product')),
                ('battery_type', models.PositiveSmallIntegerField(choices=[(1, 'LG battery'), (2, 'Chinese battery')], verbose_name='Battery type')),
                ('battery_capacity', models.DecimalField(decimal_places=1, help_text='Battery capacity in Ah', max_digits=3, null=True, verbose_name='Battery capacity')),
                ('bluetooth', models.BooleanField(default=True, help_text='Bluetooth Connectivity', verbose_name='Bluetooth')),
                ('width', models.DecimalField(decimal_places=0, help_text='Width in mm', max_digits=5, verbose_name='Width')),
                ('height', models.DecimalField(decimal_places=0, help_text='Height in mm', max_digits=5, verbose_name='Height')),
                ('weight', models.DecimalField(decimal_places=1, help_text='Weight in kg', max_digits=5, verbose_name='Weight')),
                ('max_speed', models.DecimalField(decimal_places=0, help_text='Maxumum speed in km/h', max_digits=4, verbose_name='Maxumum speed')),
                ('mileage', models.DecimalField(decimal_places=0, help_text='Maxumum mileage per one battery charge in km', max_digits=4, verbose_name='Maxumum mileage')),
                ('power', models.DecimalField(decimal_places=0, help_text='Motor power in km', max_digits=4, verbose_name='Motor power')),
                ('operating_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.OperatingSystem', verbose_name='Operating System')),
            ],
            options={
                'verbose_name': 'Electric Scooter',
                'verbose_name_plural': 'Electric Scooters',
            },
            bases=('myshop.product',),
            managers=[
                ('default_manager', django.db.models.manager.Manager()),
                ('objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ScooterModelTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('description', djangocms_text_ckeditor.fields.HTMLField(help_text="Full description used in the catalog's detail view of Scooters.", verbose_name='Description')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='multilingual', to='myshop.ScooterModel')),
            ],
            options={
                'verbose_name': 'Electric Scooter Translation',
                'db_table': 'myshop_scootermodel_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ScooterVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=255, unique=True, verbose_name='Product code')),
                ('unit_price', shop.money.fields.MoneyField(decimal_places=3, help_text='Net price for this product', verbose_name='Unit price')),
                ('battery_capacity', models.DecimalField(decimal_places=1, help_text='Battery capacity in Ah', max_digits=3, verbose_name='Battery capacity')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='myshop.ScooterModel', verbose_name='Scooter Model')),
            ],
        ),
        migrations.RenameModel(
            old_name='SmartPhoneModel2',
            new_name='SmartPhoneModel',
        ),
        migrations.RenameModel(
            old_name='SmartPhoneModel2Translation',
            new_name='SmartPhoneModelTranslation',
        ),
        migrations.AlterModelTable(
            name='smartphonemodeltranslation',
            table='myshop_smartphonemodel_translation',
        ),
        migrations.AlterUniqueTogether(
            name='scootermodeltranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
