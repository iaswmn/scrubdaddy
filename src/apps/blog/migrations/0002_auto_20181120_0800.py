# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import libs.autoslug
import libs.stdimage.fields
import libs.storages.media_storage


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='title')),
                ('last_name', libs.autoslug.AutoSlugField(unique=True, verbose_name='slug', populate_from='title')),
                ('photo', libs.stdimage.fields.StdImageField(upload_to='', blank=True, verbose_name='photo', aspects=('normal',), variations={'admin': {'size': (40, 40)}, 'normal': {'size': (40, 40)}}, storage=libs.storages.media_storage.MediaStorage('blog/photos'), min_dimensions=(40, 40))),
                ('sort_order', models.IntegerField(verbose_name='order', default=0)),
            ],
            options={
                'verbose_name': 'Author',
                'ordering': ('sort_order',),
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(verbose_name='author', to='blog.Author'),
        ),
    ]
