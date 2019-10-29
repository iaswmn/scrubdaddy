# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_in_touch', '0002_auto_20181203_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getintouchmessage',
            name='time_zone',
            field=models.CharField(blank=True, max_length=128, choices=[('ET', 'ET'), ('MT', 'MT'), ('CT', 'CT')], verbose_name='time zone'),
        ),
    ]
