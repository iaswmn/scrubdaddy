# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import libs.file_field.fields
import libs.storages.media_storage
import ckeditor.models
import libs.stdimage.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('app_name', models.CharField(verbose_name='application', max_length=30, blank=True)),
                ('model_name', models.CharField(verbose_name='model', max_length=30, blank=True)),
                ('instance_id', models.IntegerField(verbose_name='entry id', db_index=True, default=0)),
                ('file', libs.file_field.fields.FileField(verbose_name='file', blank=True, upload_to=ckeditor.models.split_by_dirs, storage=libs.storages.media_storage.MediaStorage('page_files'))),
            ],
            options={
                'verbose_name': 'page file',
                'verbose_name_plural': 'page files',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='PagePhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('app_name', models.CharField(verbose_name='application', max_length=30, blank=True)),
                ('model_name', models.CharField(verbose_name='model', max_length=30, blank=True)),
                ('instance_id', models.IntegerField(verbose_name='entry id', db_index=True, default=0)),
                ('photo', libs.stdimage.fields.StdImageField(verbose_name='image', blank=True, upload_to=ckeditor.models.split_by_dirs, storage=libs.storages.media_storage.MediaStorage('page_photos'), aspects='normal', variations={'wide': {'size': (1024, 576), 'quality': 88}, 'normal': {'size': (800, 450)}, 'mobile': {'size': (480, 270)}}, min_dimensions=(800, 450))),
                ('photo_crop', models.CharField(verbose_name='crop', max_length=32, blank=True, editable=False)),
            ],
            options={
                'verbose_name': 'page photo',
                'verbose_name_plural': 'page photos',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SimplePhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('app_name', models.CharField(verbose_name='application', max_length=30, blank=True)),
                ('model_name', models.CharField(verbose_name='model', max_length=30, blank=True)),
                ('instance_id', models.IntegerField(verbose_name='entry id', db_index=True, default=0)),
                ('photo', libs.stdimage.fields.StdImageField(verbose_name='image', blank=True, upload_to=ckeditor.models.split_by_dirs, storage=libs.storages.media_storage.MediaStorage('simple_photos'), aspects=(), variations={'mobile': {'size': (0, 0), 'crop': False, 'max_width': 512}}, max_source_dimensions=(3072, 3072))),
            ],
            options={
                'verbose_name': 'simple photo',
                'verbose_name_plural': 'simple photos',
                'default_permissions': (),
            },
        ),
    ]
