# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('where_to_buy', '0005_retailconfig_text_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='retailconfig',
            name='text_content_canada',
            field=ckeditor.fields.CKEditorField(blank=True, verbose_name='page content Canada'),
        ),
        migrations.AlterField(
            model_name='country',
            name='link',
            field=models.URLField(blank=True, verbose_name='link'),
        ),
    ]
