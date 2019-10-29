# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='year',
            field=models.CharField(verbose_name='year', blank=True, max_length=255),
        ),
    ]
