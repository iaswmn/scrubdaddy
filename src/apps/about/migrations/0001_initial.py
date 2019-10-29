# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import libs.storages.media_storage
import libs.stdimage.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('header', models.CharField(verbose_name='header', max_length=255)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
                ('text', ckeditor.fields.CKEditorUploadField(verbose_name='text', blank=True, help_text='Image sizes: from <b>800x450</b> to <b>1024x576</b>')),
            ],
            options={
                'verbose_name': 'settings',
                'abstract': False,
                'default_permissions': ('change',),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('year', models.CharField(verbose_name='year', max_length=255)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('text', models.TextField(verbose_name='text')),
                ('image', libs.stdimage.fields.StdImageField(verbose_name='image', upload_to='', storage=libs.storages.media_storage.MediaStorage('about/events'), aspects=(), variations={'normal': {'size': (240, 0), 'crop': False}, 'admin': {'size': (120, 0), 'crop': False}}, min_dimensions=(240, 240))),
                ('sort_order', models.PositiveIntegerField(verbose_name='order', default=0)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
                'ordering': ('sort_order',),
            },
        ),
    ]
