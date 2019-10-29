# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import libs.storages.media_storage
import libs.stdimage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advantage',
            name='preview',
            field=libs.stdimage.fields.StdImageField(aspects=(), variations={'normal': {'crop': False, 'size': (160, 160)}, 'admin': {'crop': False, 'size': (100, 100)}}, verbose_name='preview', min_dimensions=(160, 160), storage=libs.storages.media_storage.MediaStorage('main/preview'), upload_to=''),
        ),
    ]
