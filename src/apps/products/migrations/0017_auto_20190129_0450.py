# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_productcategory_show_on_faq_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttwofeaturesblock',
            name='text_second',
            field=ckeditor.fields.CKEditorField(verbose_name='second feature text', blank=True),
        ),
    ]
