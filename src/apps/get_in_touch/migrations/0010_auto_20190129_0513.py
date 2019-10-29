# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_in_touch', '0009_auto_20190129_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getintouchmessage',
            name='phone',
            field=models.CharField(verbose_name='phone number', max_length=32),
        ),
    ]
