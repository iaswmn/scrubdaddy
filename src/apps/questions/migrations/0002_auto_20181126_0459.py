# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20181126_0316'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='product',
        ),
        migrations.AddField(
            model_name='question',
            name='product',
            field=models.ManyToManyField(to='products.Product', verbose_name='product'),
        ),
    ]
