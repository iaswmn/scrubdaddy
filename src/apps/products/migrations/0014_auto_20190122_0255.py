# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20190122_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfeatureblock',
            name='text',
            field=ckeditor.fields.CKEditorField(verbose_name='feature text', blank=True),
        ),
        migrations.AlterField(
            model_name='producttwofeaturesblock',
            name='text',
            field=ckeditor.fields.CKEditorField(verbose_name='feature text', blank=True),
        ),
    ]
