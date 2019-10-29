# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_networks', '0002_auto_20181126_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallinks',
            name='social_google_plus',
            field=models.URLField(max_length=255, verbose_name='google plus', blank=True),
        ),
        migrations.AddField(
            model_name='sociallinks',
            name='social_yelp',
            field=models.URLField(max_length=255, verbose_name='yelp', blank=True),
        ),
        migrations.AddField(
            model_name='sociallinks',
            name='social_youtube',
            field=models.URLField(max_length=255, verbose_name='youtube', blank=True),
        ),
    ]
