# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import libs.file_field.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('employment_opportunities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='about',
            field=models.TextField(verbose_name="tell us about yourself and why you'd be a great fit \u2028for Scrub Daddy"),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='city',
            field=models.CharField(max_length=128, verbose_name='city', help_text='City'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='company_city',
            field=models.CharField(max_length=128, verbose_name='city', help_text='City'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='company_name',
            field=models.CharField(max_length=128, verbose_name='company name'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='company_phone',
            field=models.CharField(max_length=128, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='company_state',
            field=models.CharField(max_length=128, verbose_name='state', help_text='State / Province / Region'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='company_street_address',
            field=models.CharField(max_length=128, verbose_name='address', help_text='Street Address'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='company_street_address_2',
            field=models.CharField(max_length=128, verbose_name='street address 2', help_text='Street Address 2'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='company_zip_code',
            field=models.CharField(max_length=128, verbose_name='zip', help_text='Zip Code'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='contact_previous_supervisor',
            field=models.BooleanField(verbose_name='may we contact your previous supervisor for a reference?'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='date_available',
            field=models.DateTimeField(verbose_name='date available', default=datetime.datetime(2018, 12, 17, 0, 57, 59, 703983)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='desired_salary',
            field=models.CharField(max_length=128, verbose_name='desired salary'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='education',
            field=models.CharField(choices=[('Hight School', 'Hight School'), ('Associate Degree', 'Associate Degree'), ("Bachelor's Degree", "Bachelor's Degree"), ('Some College', 'Some College')], max_length=128, verbose_name='education Level'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='ending_salary',
            field=models.CharField(max_length=128, verbose_name='ending salary'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='job_title',
            field=models.CharField(max_length=128, verbose_name='your job title'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='phone',
            field=models.CharField(max_length=32, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='position',
            field=models.CharField(max_length=128, verbose_name='position applied for'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='reason_for_leaving',
            field=models.TextField(verbose_name='reason for leaving'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='responsibilities',
            field=models.TextField(verbose_name='responsibilities'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='resume',
            field=libs.file_field.fields.FileField(upload_to='employment_opportunities/resume', verbose_name='upload resume'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='school_city',
            field=models.CharField(max_length=128, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='school_name',
            field=models.CharField(max_length=128, verbose_name='school name'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='school_state',
            field=models.CharField(max_length=128, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='school_street_address',
            field=models.CharField(max_length=128, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='school_zip_code',
            field=models.CharField(max_length=128, verbose_name='zip code'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='starting_salary',
            field=models.CharField(max_length=128, verbose_name='starting salary'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='state',
            field=models.CharField(max_length=128, verbose_name='state', help_text='State / Province / Region'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='street_address',
            field=models.CharField(max_length=128, verbose_name='address', help_text='Street Address'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='street_address_2',
            field=models.CharField(max_length=128, verbose_name='street address 2', help_text='Street Address 2'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='supervisor_first_name',
            field=models.CharField(max_length=128, verbose_name="supervisor's name", help_text='First Name'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='supervisor_last_name',
            field=models.CharField(max_length=128, verbose_name='supervisor name', help_text='Last Name'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='years_attended',
            field=models.CharField(max_length=128, verbose_name='years attended', help_text='What years did you spend working at your previous job? HINT: if you worked between                    2010 to 2015, you would enter 2010-2015.'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='years_worked',
            field=models.CharField(max_length=128, verbose_name='years worked', help_text='What years did you spend working at your previous job? HINT: if you worked between                    2010 to 2015, you would enter 2010-2015.'),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='zip_code',
            field=models.CharField(max_length=128, verbose_name='zip', help_text='Zip Code'),
        ),
    ]
