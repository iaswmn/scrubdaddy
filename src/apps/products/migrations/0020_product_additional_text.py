# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20190131_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='additional_text',
            field=ckeditor.fields.CKEditorField(verbose_name='additional text', blank=True),
        ),
    ]
