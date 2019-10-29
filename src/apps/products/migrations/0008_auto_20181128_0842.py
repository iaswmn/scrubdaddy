# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import libs.stdimage.fields
import libs.storages.media_storage


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20181128_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttwofeaturesblock',
            name='preview',
            field=libs.stdimage.fields.StdImageField(min_dimensions=(580, 0), aspects=(), variations={'tablet': {'crop': False, 'size': (380, 0)}, 'admin': {'crop': False, 'size': (100, 100)}, 'normal': {'crop': False, 'size': (580, 0)}}, verbose_name='feature image', storage=libs.storages.media_storage.MediaStorage('product/features'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='producttwofeaturesblock',
            name='preview_second',
            field=libs.stdimage.fields.StdImageField(min_dimensions=(580, 0), aspects=(), variations={'tablet': {'crop': False, 'size': (380, 0)}, 'admin': {'crop': False, 'size': (100, 100)}, 'normal': {'crop': False, 'size': (580, 0)}}, verbose_name='second feature image', storage=libs.storages.media_storage.MediaStorage('product/features'), upload_to=''),
        ),
    ]
