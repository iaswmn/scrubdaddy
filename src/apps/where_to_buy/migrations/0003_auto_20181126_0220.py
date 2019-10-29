# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('where_to_buy', '0002_auto_20181123_0309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='retailshop',
            options={'verbose_name': 'shop', 'verbose_name_plural': 'shops'},
        ),
        migrations.RemoveField(
            model_name='retailshop',
            name='sort_order',
        ),
    ]
