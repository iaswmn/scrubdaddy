# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20181123_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='productconfig',
            name='text',
            field=ckeditor.fields.CKEditorField(blank=True, verbose_name='text'),
        ),
    ]
