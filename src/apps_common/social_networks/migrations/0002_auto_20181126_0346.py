# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_networks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sociallinks',
            name='social_google',
        ),
        migrations.AddField(
            model_name='sociallinks',
            name='social_linkedin',
            field=models.URLField(verbose_name='linkedin', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='sociallinks',
            name='social_pinterest',
            field=models.URLField(verbose_name='pinterest', blank=True, max_length=255),
        ),
    ]
