# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_in_touch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getintouchmessage',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='getintouchmessage',
            name='phone',
            field=models.CharField(max_length=32, verbose_name='phone number'),
        ),
    ]
