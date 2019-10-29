# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_productcategory_preview_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfeatureblock',
            name='text_position',
            field=models.CharField(max_length=64, choices=[('left', 'text-block-left'), ('right', 'text-block-right')], verbose_name='feature text position', default='left'),
        ),
    ]
