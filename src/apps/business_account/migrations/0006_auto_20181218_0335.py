# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_account', '0005_auto_20181218_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessaccountmessage',
            name='company_city',
            field=models.CharField(help_text='City', max_length=128, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='businessaccountmessage',
            name='company_country',
            field=models.CharField(help_text='Country', max_length=128, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='businessaccountmessage',
            name='company_state',
            field=models.CharField(help_text='State / Province / Region', max_length=128, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='businessaccountmessage',
            name='company_street_address_2',
            field=models.CharField(help_text='Street Address 2', max_length=128, verbose_name='street address 2'),
        ),
        migrations.AlterField(
            model_name='businessaccountmessage',
            name='company_zip',
            field=models.CharField(help_text='Zip Code', max_length=128, verbose_name='zip'),
        ),
        migrations.AlterField(
            model_name='businessaccountmessage',
            name='last_name',
            field=models.CharField(help_text='Last', max_length=128, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='businessaccountmessage',
            name='name',
            field=models.CharField(help_text='First', max_length=128, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='businessaccountmessage',
            name='registered_company_address',
            field=models.CharField(help_text='Street Address', max_length=128, verbose_name='registered street address'),
        ),
    ]
