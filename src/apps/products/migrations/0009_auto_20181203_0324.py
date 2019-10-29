# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import libs.stdimage.fields
import libs.storages.media_storage


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20181128_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='background',
            field=libs.stdimage.fields.StdImageField(aspects=(), variations={'mobile': {'crop': False, 'size': (500, 213)}, 'normal': {'crop': False, 'size': (1180, 0)}, 'admin': {'crop': False, 'size': (200, 0)}, 'tablet': {'crop': False, 'size': (768, 326)}}, verbose_name='background image', min_dimensions=(1180, 0), upload_to='', storage=libs.storages.media_storage.MediaStorage('product/features')),
        ),
        migrations.AlterField(
            model_name='productfeatureblock',
            name='background',
            field=libs.stdimage.fields.StdImageField(aspects=(), variations={'mobile': {'crop': False, 'size': (500, 213)}, 'normal': {'crop': False, 'size': (1180, 0)}, 'admin': {'crop': False, 'size': (200, 0)}, 'tablet': {'crop': False, 'size': (768, 326)}}, verbose_name='background image', min_dimensions=(1180, 0), upload_to='', storage=libs.storages.media_storage.MediaStorage('product/features')),
        ),
        migrations.AlterField(
            model_name='producttwofeaturesblock',
            name='preview',
            field=libs.stdimage.fields.StdImageField(aspects=(), variations={'mobile': {'crop': False, 'size': (400, 495)}, 'normal': {'crop': False, 'size': (580, 0)}, 'admin': {'crop': False, 'size': (100, 100)}, 'tablet': {'crop': False, 'size': (380, 470)}}, verbose_name='feature image', min_dimensions=(580, 0), upload_to='', storage=libs.storages.media_storage.MediaStorage('product/features')),
        ),
        migrations.AlterField(
            model_name='producttwofeaturesblock',
            name='preview_second',
            field=libs.stdimage.fields.StdImageField(aspects=(), variations={'mobile': {'crop': False, 'size': (400, 495)}, 'normal': {'crop': False, 'size': (580, 0)}, 'admin': {'crop': False, 'size': (100, 100)}, 'tablet': {'crop': False, 'size': (380, 470)}}, verbose_name='second feature image', min_dimensions=(580, 720), upload_to='', storage=libs.storages.media_storage.MediaStorage('product/features')),
        ),
    ]
