# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_in_touch', '0006_auto_20190129_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getintouchmessage',
            name='email',
            field=models.EmailField(verbose_name='e-mail', max_length=254),
        ),
        migrations.AlterField(
            model_name='getintouchmessage',
            name='reach_time',
            field=models.CharField(default=('11am-2pm', '11am-2pm'), verbose_name='Best time to reach you?', choices=[('8am-11am', '8am-11am'), ('11am-2pm', '11am-2pm'), ('2pm-5pm', '2pm-5pm'), ('5pm-8pm', '5pm-8pm')], max_length=32),
        ),
    ]
