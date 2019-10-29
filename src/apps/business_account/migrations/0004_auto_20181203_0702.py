# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_account', '0003_auto_20181203_0659'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thankspageconfig',
            options={'verbose_name': 'Thank you page settings', 'default_permissions': ('change',)},
        ),
        migrations.AlterField(
            model_name='thankspageconfig',
            name='page_content',
            field=models.TextField(blank=True, max_length=512, verbose_name='Page content'),
        ),
    ]
