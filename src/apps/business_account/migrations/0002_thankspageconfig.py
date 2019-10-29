# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThanksPageConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('header', models.TextField(max_length=64, verbose_name='Page header', blank=True)),
                ('content', models.TextField(max_length=128, verbose_name='Page content', blank=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='change date')),
            ],
            options={
                'verbose_name': 'settings',
                'default_permissions': ('change',),
            },
        ),
    ]
