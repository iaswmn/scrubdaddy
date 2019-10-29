# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import libs.storages.media_storage
import libs.stdimage.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaConfig',
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
        migrations.CreateModel(
            name='MediaLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('type', models.CharField(verbose_name='type', max_length=255, choices=[('VI', 'Video'), ('AU', 'Audio'), ('AR', 'Article')])),
                ('link', models.URLField(verbose_name='url')),
                ('preview', libs.stdimage.fields.StdImageField(verbose_name='preview', upload_to='', storage=libs.storages.media_storage.MediaStorage('media/previews'), aspects=(), variations={'normal': {'size': (280, 180), 'crop': True}, 'admin': {'size': (140, 90), 'crop': False}}, min_dimensions=(280, 180))),
                ('sort_order', models.PositiveIntegerField(verbose_name='order', default=0)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'media link',
                'verbose_name_plural': 'media links',
                'ordering': ('sort_order',),
            },
        ),
    ]
