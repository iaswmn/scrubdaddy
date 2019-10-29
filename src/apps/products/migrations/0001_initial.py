# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import libs.videolink_field.fields
import libs.storages.media_storage
import libs.autoslug
import libs.color_field.fields
import libs.stdimage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('attachable_blocks', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('description', models.CharField(verbose_name='description', max_length=255)),
                ('text', ckeditor.fields.CKEditorField(verbose_name='text')),
                ('preview', libs.stdimage.fields.StdImageField(verbose_name='image', upload_to='', storage=libs.storages.media_storage.MediaStorage('product/images'), aspects=(), variations={'normal': {'size': (280, 0), 'crop': False}, 'admin': {'size': (100, 0), 'crop': False}}, min_dimensions=(280, 0))),
                ('background', libs.stdimage.fields.StdImageField(verbose_name='background image', upload_to='', storage=libs.storages.media_storage.MediaStorage('product/features'), aspects=(), variations={'normal': {'size': (1180, 0), 'crop': False}, 'admin': {'size': (200, 0), 'crop': False}}, min_dimensions=(1180, 0))),
                ('link', models.URLField(verbose_name='shop url')),
                ('slug', libs.autoslug.AutoSlugField(verbose_name='slug', unique=True, populate_from='title')),
                ('sort_order', models.PositiveIntegerField(verbose_name='order', default=0)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('sort_order',),
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('description', ckeditor.fields.CKEditorUploadField(verbose_name='Description', blank=True, help_text='Image sizes: from <b>800x450</b> to <b>1024x576</b>')),
                ('slug', libs.autoslug.AutoSlugField(verbose_name='slug', unique=True, populate_from='title')),
                ('preview', libs.stdimage.fields.StdImageField(verbose_name='preview', upload_to='', storage=libs.storages.media_storage.MediaStorage('product/previews'), aspects=(), variations={'normal': {'size': (340, 370), 'crop': True}, 'admin': {'size': (170, 185), 'crop': False}}, min_dimensions=(340, 370))),
                ('background_color', libs.color_field.fields.ColorField(verbose_name='background color', blank=True, default='#FF0000')),
                ('sort_order', models.PositiveIntegerField(verbose_name='order', default=0)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('sort_order',),
            },
        ),
        migrations.CreateModel(
            name='ProductConfig',
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
            name='ProductFeatureBlock',
            fields=[
                ('attachableblock_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='attachable_blocks.AttachableBlock')),
                ('title', models.CharField(verbose_name='feature title', max_length=255)),
                ('text', models.TextField(verbose_name='feature text')),
                ('background', libs.stdimage.fields.StdImageField(verbose_name='background image', upload_to='', storage=libs.storages.media_storage.MediaStorage('product/features'), aspects=(), variations={'normal': {'size': (1180, 0), 'crop': False}, 'admin': {'size': (200, 0), 'crop': False}}, min_dimensions=(1180, 0))),
            ],
            options={
                'verbose_name': 'Product feature block',
                'verbose_name_plural': 'Product feature blocks',
            },
            bases=('attachable_blocks.attachableblock',),
        ),
        migrations.CreateModel(
            name='ProductTwoFeaturesBlock',
            fields=[
                ('attachableblock_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='attachable_blocks.AttachableBlock')),
                ('title', models.CharField(verbose_name='feature title', max_length=255)),
                ('text', models.TextField(verbose_name='feature text')),
                ('preview', libs.stdimage.fields.StdImageField(verbose_name='feature image', upload_to='', storage=libs.storages.media_storage.MediaStorage('product/features'), aspects=(), variations={'normal': {'size': (280, 340), 'crop': True}, 'admin': {'size': (100, 100), 'crop': False}}, min_dimensions=(280, 0))),
                ('title_second', models.CharField(verbose_name='second feature title', max_length=255)),
                ('text_second', models.TextField(verbose_name='second feature text')),
                ('preview_second', libs.stdimage.fields.StdImageField(verbose_name='second feature image', upload_to='', storage=libs.storages.media_storage.MediaStorage('product/features'), aspects=(), variations={'normal': {'size': (280, 340), 'crop': True}, 'admin': {'size': (100, 100), 'crop': False}}, min_dimensions=(280, 0))),
            ],
            options={
                'verbose_name': 'Product two features block',
                'verbose_name_plural': 'Product two features blocks',
            },
            bases=('attachable_blocks.attachableblock',),
        ),
        migrations.CreateModel(
            name='ProductVideoBlock',
            fields=[
                ('attachableblock_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='attachable_blocks.AttachableBlock')),
                ('video', libs.videolink_field.fields.VideoLinkField(verbose_name='video', providers=set(['youtube']))),
            ],
            options={
                'verbose_name': 'Product video block',
                'verbose_name_plural': 'Product video blocks',
            },
            bases=('attachable_blocks.attachableblock',),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(verbose_name='category', related_name='products', to='products.ProductCategory'),
        ),
    ]
