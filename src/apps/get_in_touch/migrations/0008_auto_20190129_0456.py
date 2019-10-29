# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_in_touch', '0007_auto_20190129_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getintouchmessage',
            name='time_zone',
            field=models.CharField(default=('MT', 'MT'), choices=[('ET', 'ET'), ('MT', 'MT'), ('CT', 'CT'), ('PT', 'PT')], max_length=128, verbose_name='time zone'),
        ),
    ]
