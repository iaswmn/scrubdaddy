# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('where_to_buy', '0006_auto_20181214_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailconfig',
            name='text_content',
            field=ckeditor.fields.CKEditorField(verbose_name='page content USA', blank=True),
        ),
    ]
