# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_productcategory_show_button'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='show_button',
        ),
        migrations.AddField(
            model_name='product',
            name='show_button',
            field=models.BooleanField(default=True, verbose_name='show shop me button'),
        ),
    ]
