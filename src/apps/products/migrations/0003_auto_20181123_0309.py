# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20181122_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_in_canada',
            field=models.BooleanField(verbose_name='available in canada', default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='available_in_usa',
            field=models.BooleanField(verbose_name='available in usa', default=True),
        ),
    ]
