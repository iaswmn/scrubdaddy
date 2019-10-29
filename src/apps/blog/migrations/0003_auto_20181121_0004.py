# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181120_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(to='blog.Author', null=True, blank=True, verbose_name='author'),
        ),
    ]
