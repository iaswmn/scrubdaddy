# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_productfeatureblock_text_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfeatureblock',
            name='text',
            field=models.TextField(verbose_name='feature text', blank=True),
        ),
        migrations.AlterField(
            model_name='productfeatureblock',
            name='text_position',
            field=models.CharField(max_length=64, choices=[('left', 'left'), ('right', 'right')], verbose_name='feature text position', default='left'),
        ),
        migrations.AlterField(
            model_name='productfeatureblock',
            name='title',
            field=models.CharField(max_length=255, verbose_name='feature title', blank=True),
        ),
    ]
