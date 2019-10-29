# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment_opportunities', '0003_auto_20190131_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='employmentopportunitiesmessage',
            name='company_country',
            field=models.CharField(verbose_name='country', max_length=128, help_text='Country', default=' '),
            preserve_default=False,
        ),
    ]
