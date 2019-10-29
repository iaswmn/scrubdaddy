# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment_opportunities', '0002_auto_20181217_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='felony',
            field=models.BooleanField(verbose_name='have you ever been convicted of a felony?', default=False),
        ),
        migrations.AlterField(
            model_name='employmentopportunitiesmessage',
            name='worked',
            field=models.BooleanField(verbose_name='have you ever worked for this company?', default=False),
        ),
    ]
