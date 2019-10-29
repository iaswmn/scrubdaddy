# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20190122_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='show_on_faq_page',
            field=models.BooleanField(verbose_name='show on FAQ page', default=True),
        ),
    ]
