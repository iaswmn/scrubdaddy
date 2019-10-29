# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_account', '0004_auto_20181203_0702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessaccountmessage',
            name='agreement_first_name',
        ),
        migrations.RemoveField(
            model_name='businessaccountmessage',
            name='agreement_last_name',
        ),
    ]
