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
            name='EmploymentOpportunitiesConfig',
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
            name='EmploymentOpportunitiesMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(verbose_name='name', max_length=128, help_text='First')),
                ('last_name', models.CharField(verbose_name='last name', max_length=128, help_text='Last')),
                ('street_address', models.CharField(verbose_name='address', max_length=128, blank=True, help_text='Street Address')),
                ('street_address_2', models.CharField(verbose_name='street address 2', max_length=128, blank=True, help_text='Street Address 2')),
                ('city', models.CharField(verbose_name='city', max_length=128, blank=True, help_text='City')),
                ('state', models.CharField(verbose_name='state', max_length=128, blank=True, help_text='State / Province / Region')),
                ('zip_code', models.CharField(verbose_name='zip', max_length=128, blank=True, help_text='Zip Code')),
                ('phone', models.CharField(verbose_name='phone', max_length=32, blank=True)),
                ('date_available', models.DateTimeField(verbose_name='date available', blank=True, null=True)),
                ('desired_salary', models.CharField(verbose_name='desired salary', max_length=128, blank=True)),
                ('email', models.EmailField(verbose_name='email', max_length=254, blank=True)),
                ('position', models.CharField(verbose_name='position applied for', max_length=128, blank=True)),
                ('about', models.TextField(verbose_name="tell us about yourself and why you'd be a great fit \u2028for Scrub Daddy", blank=True)),
                ('citizen', models.BooleanField(verbose_name='are you a citizen of the United States?', default=False)),
                ('worked', models.BooleanField(verbose_name='have you ever worked for this company', default=False)),
                ('felony', models.BooleanField(verbose_name='have you ever been convicted of a felony', default=False)),
                ('education', models.CharField(verbose_name='education Level', max_length=128, blank=True, choices=[('Hight School', 'Hight School'), ('Associate Degree', 'Associate Degree'), ("Bachelor's Degree", "Bachelor's Degree"), ('Some College', 'Some College')])),
                ('school_name', models.CharField(verbose_name='school name', max_length=128, blank=True)),
                ('school_street_address', models.CharField(verbose_name='address', max_length=128, blank=True)),
                ('school_city', models.CharField(verbose_name='city', max_length=128, blank=True)),
                ('school_state', models.CharField(verbose_name='state', max_length=128, blank=True)),
                ('school_zip_code', models.CharField(verbose_name='zip code', max_length=128, blank=True)),
                ('years_attended', models.CharField(verbose_name='years attended', max_length=128, blank=True, help_text='What years did you spend working at your previous job? HINT: if you worked between                    2010 to 2015, you would enter 2010-2015.')),
                ('company_name', models.CharField(verbose_name='company name', max_length=128, blank=True)),
                ('company_phone', models.CharField(verbose_name='phone', max_length=128, blank=True)),
                ('company_street_address', models.CharField(verbose_name='address', max_length=128, blank=True, help_text='Street Address')),
                ('company_street_address_2', models.CharField(verbose_name='street address 2', max_length=128, blank=True, help_text='Street Address 2')),
                ('company_city', models.CharField(verbose_name='city', max_length=128, blank=True, help_text='City')),
                ('company_state', models.CharField(verbose_name='state', max_length=128, blank=True, help_text='State / Province / Region')),
                ('company_zip_code', models.CharField(verbose_name='zip', max_length=128, blank=True, help_text='Zip Code')),
                ('supervisor_first_name', models.CharField(verbose_name="supervisor's name", max_length=128, blank=True, help_text='First Name')),
                ('supervisor_last_name', models.CharField(verbose_name='supervisor name', max_length=128, blank=True, help_text='Last Name')),
                ('job_title', models.CharField(verbose_name='your job title', max_length=128, blank=True)),
                ('starting_salary', models.CharField(verbose_name='starting salary', max_length=128, blank=True)),
                ('years_worked', models.CharField(verbose_name='years worked', max_length=128, blank=True, help_text='What years did you spend working at your previous job? HINT: if you worked between                    2010 to 2015, you would enter 2010-2015.')),
                ('ending_salary', models.CharField(verbose_name='ending salary', max_length=128, blank=True)),
                ('responsibilities', models.TextField(verbose_name='responsibilities', blank=True)),
                ('reason_for_leaving', models.TextField(verbose_name='reason for leaving', blank=True)),
                ('contact_previous_supervisor', models.BooleanField(verbose_name='may we contact your previous supervisor for a reference?', default=False)),
                ('resume', libs.file_field.fields.FileField(verbose_name='upload resume', blank=True, null=True, upload_to='employment_opportunities/resume')),
                ('user_date', models.DateTimeField(verbose_name="today's date", blank=True, null=True)),
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
            name='EmploymentOpportunitiesSignature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('file', libs.file_field.fields.FileField(verbose_name='signature', upload_to='employment_opportunities/signatures')),
                ('created', models.DateTimeField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('message', models.ForeignKey(related_name='signatures', to='employment_opportunities.EmploymentOpportunitiesMessage')),
            ],
            options={
                'verbose_name': 'Signature',
                'verbose_name_plural': 'Signatures',
                'ordering': ('-created',),
                'default_permissions': ('delete',),
            },
        ),
    ]
