# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('where_to_buy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='retailshop',
            name='available_in_canada',
            field=models.BooleanField(verbose_name='available in canada', default=True),
        ),
        migrations.AddField(
            model_name='retailshop',
            name='available_in_usa',
            field=models.BooleanField(verbose_name='available in usa', default=True),
        ),
    ]
