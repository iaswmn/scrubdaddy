# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_hint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='title'),
        ),
    ]
