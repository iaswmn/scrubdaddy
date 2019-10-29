# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import libs.storages.media_storage
import libs.stdimage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190226_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainslider',
            name='slide_title',
            field=models.TextField(verbose_name='slide title for inner use', default='slide', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mainslider',
            name='background',
            field=libs.stdimage.fields.StdImageField(verbose_name='background', upload_to='', storage=libs.storages.media_storage.MediaStorage('main_slider/background'), variations={'normal': {'crop': True, 'size': (1920, 0)}, 'admin': {'crop': False, 'size': (480, 115)}, 'mobile': {'crop': False, 'size': (320, 0)}, 'tablet': {'crop': False, 'size': (1400, 0)}}, aspects=(), min_dimensions=(400, 400)),
        ),
        migrations.AlterField(
            model_name='mainslider',
            name='is_small_slide',
            field=models.BooleanField(default=False, verbose_name='small picture'),
        ),
        migrations.AlterField(
            model_name='mainslider',
            name='title',
            field=models.TextField(blank=True, verbose_name='title', max_length=255),
        ),
    ]
