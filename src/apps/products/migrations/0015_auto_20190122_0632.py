# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20190122_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='text',
            field=models.TextField(blank=True, verbose_name='text'),
        ),
    ]
