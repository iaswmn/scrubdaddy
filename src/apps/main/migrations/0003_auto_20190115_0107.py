# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20181121_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpageconfig',
            name='advantages_title',
            field=ckeditor.fields.CKEditorField(verbose_name='advantages title'),
        ),
    ]
