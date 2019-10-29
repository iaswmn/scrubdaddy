# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20181224_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='preview_alt',
            field=models.CharField(blank=True, max_length=255, verbose_name='preview img alt'),
        ),
    ]
