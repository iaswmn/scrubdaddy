# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productconfig_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='text',
            field=ckeditor.fields.CKEditorField(verbose_name='text', blank=True),
        ),
    ]
