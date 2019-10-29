# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190115_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='advantage',
            name='preview_alt',
            field=models.CharField(max_length=255, blank=True, verbose_name='preview alt'),
        ),
    ]
