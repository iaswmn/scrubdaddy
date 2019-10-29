# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20181121_0311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='getintouchmessageimage',
            name='message',
        ),
        migrations.DeleteModel(
            name='GetInTouchMessageImage',
        ),
    ]
