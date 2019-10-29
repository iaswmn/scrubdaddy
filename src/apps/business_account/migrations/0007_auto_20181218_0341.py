# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_account', '0006_auto_20181218_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessaccountmessage',
            name='website',
            field=models.CharField(max_length=32, verbose_name='website'),
        ),
    ]
