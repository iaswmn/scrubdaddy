# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import libs.file_field.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessAccountConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('header', models.CharField(verbose_name='header', max_length=255)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'settings',
                'abstract': False,
                'default_permissions': ('change',),
            },
        ),
        migrations.CreateModel(
            name='BusinessAccountMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=128, blank=True, help_text='First')),
                ('last_name', models.CharField(verbose_name='last name', max_length=128, blank=True, help_text='Last')),
                ('title', models.CharField(verbose_name='title', max_length=128)),
                ('company_name', models.CharField(verbose_name='company name', max_length=128)),
                ('date_of_commencement', models.DateTimeField(verbose_name='date of commencement')),
                ('registered_company_address', models.CharField(verbose_name='registered street address', max_length=128, blank=True, help_text='Street Address')),
                ('company_street_address_2', models.CharField(verbose_name='street address 2', max_length=128, blank=True, help_text='Street Address 2')),
                ('company_city', models.CharField(verbose_name='city', max_length=128, blank=True, help_text='City')),
                ('company_state', models.CharField(verbose_name='state', max_length=128, blank=True, help_text='State / Province / Region')),
                ('company_zip', models.CharField(verbose_name='zip', max_length=128, blank=True, help_text='Zip Code')),
                ('company_country', models.CharField(verbose_name='country', max_length=128, blank=True, help_text='Country')),
                ('phone', models.CharField(verbose_name='phone', max_length=32)),
                ('email', models.EmailField(verbose_name='Email', max_length=254)),
                ('fax', models.CharField(verbose_name='fax', max_length=32, blank=True)),
                ('website', models.CharField(verbose_name='website', max_length=32, blank=True)),
                ('wholesale', models.BooleanField(verbose_name='wholesale', default=False)),
                ('distributor', models.BooleanField(verbose_name='distributor', default=False)),
                ('retailer', models.BooleanField(verbose_name='retailer', default=False)),
                ('broker', models.BooleanField(verbose_name='broker', default=False)),
                ('trade_reference_company_name', models.CharField(verbose_name='Company name', max_length=128)),
                ('trade_reference_street_address', models.CharField(verbose_name='Address', max_length=128, help_text='Street Address')),
                ('trade_reference_street_address_2', models.CharField(verbose_name='trade reference street address 2', max_length=128, help_text='Street Address 2')),
                ('trade_reference_city', models.CharField(verbose_name='trade reference city', max_length=128, help_text='City')),
                ('trade_reference_state', models.CharField(verbose_name='trade reference state', max_length=128, help_text='State / Province / Region')),
                ('trade_reference_zip', models.CharField(verbose_name='trade reference zip', max_length=128, help_text='Zip Code')),
                ('trade_reference_country', models.CharField(verbose_name='trade reference country', max_length=128, help_text='Country')),
                ('trade_reference_phone', models.CharField(verbose_name='Phone', max_length=32)),
                ('trade_reference_email', models.EmailField(verbose_name='Email', max_length=254)),
                ('trade_reference_fax', models.CharField(verbose_name='Fax', max_length=32, blank=True)),
                ('trade_reference_2_company_name', models.CharField(verbose_name='Company name', max_length=128)),
                ('trade_reference_2_street_address', models.CharField(verbose_name='Address', max_length=128, help_text='Street Address')),
                ('trade_reference_2_street_address_2', models.CharField(verbose_name='Address 2', max_length=128, help_text='Street Address 2')),
                ('trade_reference_2_city', models.CharField(verbose_name='City', max_length=128, help_text='City')),
                ('trade_reference_2_state', models.CharField(verbose_name='State', max_length=128, help_text='State / Province / Region')),
                ('trade_reference_2_zip', models.CharField(verbose_name='Zip', max_length=128, help_text='Zip Code')),
                ('trade_reference_2_country', models.CharField(verbose_name='Country', max_length=128, help_text='Country')),
                ('trade_reference_2_phone', models.CharField(verbose_name='Phone', max_length=32)),
                ('trade_reference_2_email', models.EmailField(verbose_name='Email', max_length=254)),
                ('trade_reference_2_fax', models.CharField(verbose_name='Fax', max_length=32, blank=True)),
                ('agreement_first_name', models.CharField(verbose_name='Your name', max_length=128, help_text='First')),
                ('agreement_last_name', models.CharField(verbose_name='agreement last name', max_length=128, help_text='Last')),
                ('date', models.DateTimeField(verbose_name='date sent', default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
                'ordering': ('-date',),
                'default_permissions': ('delete',),
            },
        ),
        migrations.CreateModel(
            name='BusinessAccountMessageSignature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('file', libs.file_field.fields.FileField(verbose_name='signature', upload_to='business_account/signatures')),
                ('created', models.DateTimeField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('message', models.ForeignKey(related_name='signatures', to='business_account.BusinessAccountMessage')),
            ],
            options={
                'verbose_name': 'Signature',
                'verbose_name_plural': 'Signatures',
                'ordering': ('-created',),
                'default_permissions': ('delete',),
            },
        ),
    ]
