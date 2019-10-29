# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('country', django_countries.fields.CountryField(verbose_name='country', max_length=2)),
                ('link', models.URLField(verbose_name='link')),
                ('sort_order', models.PositiveIntegerField(verbose_name='order', default=0)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'county',
                'verbose_name_plural': 'countries',
                'ordering': ('sort_order',),
            },
        ),
        migrations.CreateModel(
            name='InternationalConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('header', models.CharField(verbose_name='header', max_length=255)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'International',
                'abstract': False,
                'default_permissions': ('change',),
            },
        ),
        migrations.CreateModel(
            name='OnlineShopConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('header', models.CharField(verbose_name='header', max_length=255)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'Online Smile Shop',
                'abstract': False,
                'default_permissions': ('change',),
            },
        ),
        migrations.CreateModel(
            name='RetailConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('header', models.CharField(verbose_name='header', max_length=255)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'Retail',
                'abstract': False,
                'default_permissions': ('change',),
            },
        ),
        migrations.CreateModel(
            name='RetailShop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('sort_order', models.PositiveIntegerField(verbose_name='order', default=0)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'shop',
                'verbose_name_plural': 'shops',
                'ordering': ('sort_order',),
            },
        ),
    ]
