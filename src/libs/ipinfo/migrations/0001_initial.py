# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-25 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IpInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(unique=True, verbose_name='ip')),
                ('city', models.CharField(max_length=255, verbose_name='city')),
                ('region', models.CharField(max_length=255, verbose_name='region')),
                ('country', models.CharField(max_length=255, verbose_name='country')),
                ('latitude', models.DecimalField(decimal_places=4, max_digits=8, verbose_name='latitude')),
                ('longitude', models.DecimalField(decimal_places=4, max_digits=8, verbose_name='longitude')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
            ],
            options={
                'verbose_name': 'IpInfo',
                'verbose_name_plural': 'IpInfo',
            },
        ),
        migrations.AlterUniqueTogether(
            name='ipinfo',
            unique_together=set([('ip', 'updated')]),
        ),
    ]