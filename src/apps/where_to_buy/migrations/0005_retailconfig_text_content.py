# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('where_to_buy', '0004_retailconfig_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='retailconfig',
            name='text_content',
            field=ckeditor.fields.CKEditorField(verbose_name='page content', blank=True),
        ),
    ]
