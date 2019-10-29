# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import libs.storages.media_storage
import libs.autoslug
import django.utils.timezone
import libs.stdimage.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('header', models.CharField(verbose_name='header', max_length=255)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'Settings',
                'default_permissions': ('change',),
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('header', models.CharField(verbose_name='header', max_length=255)),
                ('slug', libs.autoslug.AutoSlugField(verbose_name='slug', unique=True, populate_from='header')),
                ('note', models.TextField(verbose_name='note')),
                ('text', ckeditor.fields.CKEditorUploadField(verbose_name='text', help_text='Image sizes: from <b>800x450</b> to <b>1024x576</b>')),
                ('date', models.DateTimeField(verbose_name='publication date', default=django.utils.timezone.now)),
                ('status', models.IntegerField(verbose_name='status', default=1, choices=[(1, 'Draft'), (2, 'Public')])),
                ('preview', libs.stdimage.fields.StdImageField(verbose_name='preview', blank=True, upload_to='', storage=libs.storages.media_storage.MediaStorage('blog/preview'), aspects=('normal',), variations={'normal': {'size': (900, 500)}, 'mobile': {'size': (540, 300)}, 'admin': {'size': (450, 250)}}, min_dimensions=(900, 500))),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ('-date', '-id'),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('slug', libs.autoslug.AutoSlugField(verbose_name='slug', unique=True, populate_from='title')),
                ('sort_order', models.IntegerField(verbose_name='order', default=0)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ('sort_order',),
            },
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(verbose_name='tags', related_name='posts', to='blog.Tag'),
        ),
    ]
