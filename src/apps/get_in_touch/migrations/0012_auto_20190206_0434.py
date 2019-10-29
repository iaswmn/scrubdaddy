# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_in_touch', '0011_auto_20190131_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getintouchmessage',
            name='reach_time',
            field=models.CharField(blank=True, verbose_name='Best time to reach you?', choices=[('8am-11am', '8am-11am'), ('11am-2pm', '11am-2pm'), ('2pm-5pm', '2pm-5pm'), ('5pm-8pm', '5pm-8pm')], max_length=32),
        ),
        migrations.AlterField(
            model_name='getintouchmessage',
            name='time_zone',
            field=models.CharField(blank=True, verbose_name='time zone', choices=[('ET', 'ET'), ('MT', 'MT'), ('CT', 'CT'), ('PT', 'PT')], max_length=128),
        ),
    ]
