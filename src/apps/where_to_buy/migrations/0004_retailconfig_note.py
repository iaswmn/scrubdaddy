# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('where_to_buy', '0003_auto_20181126_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='retailconfig',
            name='note',
            field=models.TextField(blank=True, verbose_name='note'),
        ),
    ]
