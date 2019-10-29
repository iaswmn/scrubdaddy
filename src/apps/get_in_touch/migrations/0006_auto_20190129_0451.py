# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_in_touch', '0005_auto_20190122_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getintouchmessage',
            name='reach_time',
            field=models.CharField(choices=[('8am-11am', '8am-11am'), ('11am-2pm', '11am-2pm'), ('2pm-5pm', '2pm-5pm'), ('5pm-8pm', '5pm-8pm')], max_length=32, blank=True, verbose_name='Best time to reach you?'),
        ),
    ]
