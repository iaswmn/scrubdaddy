# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_account', '0002_thankspageconfig'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thankspageconfig',
            options={'verbose_name': 'Thank you page setting', 'default_permissions': ('change',)},
        ),
        migrations.RenameField(
            model_name='thankspageconfig',
            old_name='content',
            new_name='page_content',
        ),
    ]
