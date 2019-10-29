# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20181205_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=ckeditor.fields.CKEditorUploadField(verbose_name='text', help_text='Image sizes: from <b>800x450</b> to <b>1024x576</b>'),
        ),
    ]
