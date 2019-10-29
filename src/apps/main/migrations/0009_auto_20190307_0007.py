# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_mainslider_learn_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainslider',
            name='product',
            field=models.ForeignKey(verbose_name='product', blank=True, null=True, related_name='slides', to='products.Product'),
        ),
    ]
