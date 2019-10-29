# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20181123_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonenumber',
            name='phone_word',
            field=models.CharField(blank=True, max_length=16, verbose_name='phone word'),
        ),
    ]
