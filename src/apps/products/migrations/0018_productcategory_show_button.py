# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20190129_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='show_button',
            field=models.BooleanField(verbose_name='show shop me button', default=True),
        ),
    ]
