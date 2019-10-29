# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20181126_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=ckeditor.fields.CKEditorField(verbose_name='text'),
        ),
    ]
