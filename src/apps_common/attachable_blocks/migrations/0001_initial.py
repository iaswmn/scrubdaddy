# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttachableBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('label', models.CharField(verbose_name='label', max_length=128, help_text='For inner use')),
                ('visible', models.BooleanField(verbose_name='visible', default=True)),
                ('created', models.DateTimeField(verbose_name='create date', editable=False)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
                ('content_type', models.ForeignKey(null=True, editable=False, related_name='+', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'attachable block',
                'verbose_name_plural': 'attachable blocks',
                'ordering': ('label',),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='AttachableReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('object_id', models.IntegerField()),
                ('ajax', models.BooleanField(verbose_name='AJAX', default=False, help_text='load block via AJAX')),
                ('set_name', models.CharField(verbose_name='set name', max_length=32, default='default')),
                ('sort_order', models.IntegerField(verbose_name='sort order', default=0)),
                ('block', models.ForeignKey(verbose_name='block', related_name='references', to='attachable_blocks.AttachableBlock')),
                ('block_ct', models.ForeignKey(null=True, related_name='+', to='contenttypes.ContentType')),
                ('content_type', models.ForeignKey(related_name='+', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'attached block',
                'verbose_name_plural': 'attached blocks',
                'ordering': ('set_name', 'sort_order'),
            },
        ),
        migrations.AlterIndexTogether(
            name='attachablereference',
            index_together=set([('content_type', 'object_id', 'set_name')]),
        ),
    ]
