# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20181203_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='title',
            field=models.TextField(verbose_name='title', max_length=255),
        ),
    ]
