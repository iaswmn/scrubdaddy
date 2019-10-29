# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20181126_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttwofeaturesblock',
            name='text_second',
            field=models.TextField(verbose_name='second feature text', blank=True),
        ),
        migrations.AlterField(
            model_name='producttwofeaturesblock',
            name='title_second',
            field=models.CharField(max_length=255, verbose_name='second feature title', blank=True),
        ),
    ]
