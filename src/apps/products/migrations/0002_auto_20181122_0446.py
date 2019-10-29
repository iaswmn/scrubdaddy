# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import libs.stdimage.fields
import libs.storages.media_storage


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttwofeaturesblock',
            name='preview',
            field=libs.stdimage.fields.StdImageField(aspects=(), verbose_name='feature image', min_dimensions=(580, 0), variations={'admin': {'crop': False, 'size': (100, 100)}, 'normal': {'crop': False, 'size': (580, 0)}}, upload_to='', storage=libs.storages.media_storage.MediaStorage('product/features')),
        ),
        migrations.AlterField(
            model_name='producttwofeaturesblock',
            name='preview_second',
            field=libs.stdimage.fields.StdImageField(aspects=(), verbose_name='second feature image', min_dimensions=(580, 0), variations={'admin': {'crop': False, 'size': (100, 100)}, 'normal': {'crop': False, 'size': (580, 0)}}, upload_to='', storage=libs.storages.media_storage.MediaStorage('product/features')),
        ),
    ]
