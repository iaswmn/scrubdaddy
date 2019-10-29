# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import libs.storages.media_storage
import libs.stdimage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('text', models.TextField(verbose_name='text')),
                ('active', models.BooleanField(verbose_name='active', default=False)),
                ('visible', models.BooleanField(verbose_name='visible', default=True)),
                ('image', libs.stdimage.fields.StdImageField(verbose_name='image', blank=True, null=True, upload_to='', storage=libs.storages.media_storage.MediaStorage('questions/images'), aspects=(), variations={'normal': {'size': (650, 0), 'crop': False}, 'admin': {'size': (200, 0), 'crop': False}}, min_dimensions=(650, 0))),
                ('sort_order', models.PositiveIntegerField(verbose_name='order', default=0)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
                ('product', models.ForeignKey(verbose_name='product', to='products.Product')),
            ],
            options={
                'verbose_name': 'question',
                'verbose_name_plural': 'questions',
                'ordering': ('sort_order',),
            },
        ),
        migrations.CreateModel(
            name='QuestionsConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('header', models.CharField(verbose_name='header', max_length=255)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'settings',
                'abstract': False,
                'default_permissions': ('change',),
            },
        ),
    ]
