# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_in_touch', '0003_auto_20181203_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getintouchmessage',
            name='email',
            field=models.EmailField(verbose_name='e-mail', max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='getintouchmessage',
            name='phone',
            field=models.CharField(verbose_name='phone number', max_length=32, blank=True),
        ),
        migrations.AlterField(
            model_name='getintouchmessage',
            name='reach_time',
            field=models.CharField(verbose_name='Best time to reach you?', max_length=128, blank=True),
        ),
    ]
