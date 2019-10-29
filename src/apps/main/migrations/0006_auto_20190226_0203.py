# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import libs.storages.media_storage
import libs.stdimage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_advantage_preview_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainslider',
            name='is_small_slide',
            field=models.BooleanField(default=False, verbose_name='slide style'),
        ),
        migrations.AlterField(
            model_name='mainslider',
            name='background',
            field=libs.stdimage.fields.StdImageField(min_dimensions=(400, 400), variations={'mobile': {'crop': False, 'size': (320, 0)}, 'tablet': {'crop': False, 'size': (1400, 0)}, 'admin': {'crop': False, 'size': (480, 115)}, 'small_slide': {'crop': False, 'size': (580, 520)}, 'normal': {'crop': False, 'size': (1920, 0)}}, verbose_name='background', storage=libs.storages.media_storage.MediaStorage('main_slider/background'), aspects=(), upload_to=''),
        ),
    ]
