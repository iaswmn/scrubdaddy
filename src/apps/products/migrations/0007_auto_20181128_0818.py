# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20181128_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttwofeaturesblock',
            name='text',
            field=models.TextField(blank=True, verbose_name='feature text'),
        ),
        migrations.AlterField(
            model_name='producttwofeaturesblock',
            name='title',
            field=models.CharField(verbose_name='feature title', blank=True, max_length=255),
        ),
    ]
