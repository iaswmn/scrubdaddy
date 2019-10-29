# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import libs.storages.media_storage
import libs.stdimage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('description', models.TextField(verbose_name='description')),
                ('preview', libs.stdimage.fields.StdImageField(verbose_name='preview', upload_to='', storage=libs.storages.media_storage.MediaStorage('main/preview'), aspects=(), variations={'normal': {'size': (128, 128), 'crop': False}, 'admin': {'size': (100, 100), 'crop': False}}, min_dimensions=(128, 128))),
                ('sort_order', models.PositiveIntegerField(verbose_name='order', default=0)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'advantage',
                'verbose_name_plural': 'advantages',
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='MainPageConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('advantages_title', models.CharField(verbose_name='advantages title', max_length=255)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'settings',
                'default_permissions': ('change',),
            },
        ),
        migrations.CreateModel(
            name='MainSlider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('background', libs.stdimage.fields.StdImageField(verbose_name='background', upload_to='', storage=libs.storages.media_storage.MediaStorage('main_slider/background'), aspects=(), variations={'normal': {'size': (1920, 0), 'crop': False}, 'tablet': {'size': (1400, 0), 'crop': False}, 'mobile': {'size': (320, 0), 'crop': False}, 'admin': {'size': (480, 115), 'crop': False}}, min_dimensions=(1920, 460))),
                ('background_alt', models.CharField(verbose_name='background alt', max_length=255, blank=True, help_text='for SEO')),
                ('order', models.PositiveSmallIntegerField()),
                ('product', models.ForeignKey(verbose_name='product', related_name='slides', to='products.Product')),
            ],
            options={
                'verbose_name': 'slider',
                'verbose_name_plural': 'Slider',
                'ordering': ['order'],
            },
        ),
    ]
