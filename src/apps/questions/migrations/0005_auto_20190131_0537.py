# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20190129_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='product',
            field=models.ManyToManyField(verbose_name='product', to='products.Product', blank=True),
        ),
    ]
