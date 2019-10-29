# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190226_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainslider',
            name='learn_more',
            field=models.BooleanField(verbose_name='Button Learn More', default=True),
        ),
    ]
