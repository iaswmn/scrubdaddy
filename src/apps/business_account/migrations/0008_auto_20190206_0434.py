# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_account', '0007_auto_20181218_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessaccountmessage',
            name='company_street_address_2',
            field=models.CharField(help_text='Street Address 2', blank=True, verbose_name='street address 2', max_length=128),
        ),
        migrations.AlterField(
            model_name='businessaccountmessage',
            name='trade_reference_2_street_address_2',
            field=models.CharField(help_text='Street Address 2', blank=True, verbose_name='Address 2', max_length=128),
        ),
        migrations.AlterField(
            model_name='businessaccountmessage',
            name='trade_reference_street_address_2',
            field=models.CharField(help_text='Street Address 2', blank=True, verbose_name='trade reference street address 2', max_length=128),
        ),
    ]
