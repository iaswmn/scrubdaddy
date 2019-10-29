# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import google_maps.fields
import libs.storages.media_storage
import libs.file_field.fields
import django.utils.timezone
import libs.multiselect_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('attachable_blocks', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('address', models.CharField(verbose_name='address', max_length=255)),
                ('city', models.CharField(verbose_name='city', max_length=255)),
                ('region', models.CharField(verbose_name='region', max_length=64, blank=True)),
                ('zip', models.CharField(verbose_name='zip', max_length=32, blank=True)),
                ('coords', google_maps.fields.GoogleCoordsField(verbose_name='coords', blank=True, help_text='Double click on the map places marker')),
                ('sort_order', models.PositiveIntegerField(verbose_name='sort order')),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
                'ordering': ('sort_order',),
            },
        ),
        migrations.CreateModel(
            name='ContactBlock',
            fields=[
                ('attachableblock_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='attachable_blocks.AttachableBlock')),
                ('header', models.CharField(verbose_name='header', max_length=128, blank=True)),
            ],
            options={
                'verbose_name': 'Contact block',
                'verbose_name_plural': 'Contact blocks',
            },
            bases=('attachable_blocks.attachableblock',),
        ),
        migrations.CreateModel(
            name='ContactsConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('header', models.CharField(verbose_name='header', max_length=128)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'settings',
                'default_permissions': ('change',),
            },
        ),
        migrations.CreateModel(
            name='GetInTouchMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=128)),
                ('phone', models.CharField(verbose_name='phone', max_length=32, blank=True)),
                ('email', models.EmailField(verbose_name='e-mail', max_length=254, blank=True)),
                ('comments', models.TextField(verbose_name='comments', max_length=2048)),
                ('reach_type', models.CharField(verbose_name='reach type', max_length=128, choices=[('Phone', 'Phone'), ('Email', 'Email')], help_text='Hint: Inquiries are best answered with a quick chat!')),
                ('reach_time', models.CharField(verbose_name='reach time', max_length=128)),
                ('time_zone', models.CharField(verbose_name='time zone', max_length=128, choices=[('ET', 'ET'), ('MT', 'MT'), ('CT', 'CT')])),
                ('date', models.DateTimeField(verbose_name='date sent', default=django.utils.timezone.now, editable=False)),
                ('referer', models.CharField(verbose_name='from page', max_length=512, blank=True, editable=False)),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
                'ordering': ('-date',),
                'default_permissions': ('delete',),
            },
        ),
        migrations.CreateModel(
            name='GetInTouchMessageImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('file', libs.file_field.fields.ImageField(verbose_name='image', upload_to='', storage=libs.storages.media_storage.MediaStorage('contacts/images'))),
                ('created', models.DateTimeField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('message', models.ForeignKey(related_name='images', to='contacts.GetInTouchMessage')),
            ],
            options={
                'verbose_name': 'get in touch image',
                'verbose_name_plural': 'get in touch images',
                'ordering': ('-created',),
                'default_permissions': ('delete',),
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=128)),
                ('phone', models.CharField(verbose_name='phone', max_length=32, blank=True)),
                ('email', models.EmailField(verbose_name='e-mail', max_length=254, blank=True)),
                ('message', models.TextField(verbose_name='message', max_length=2048)),
                ('date', models.DateTimeField(verbose_name='date sent', default=django.utils.timezone.now, editable=False)),
                ('referer', models.CharField(verbose_name='from page', max_length=512, blank=True, editable=False)),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
                'ordering': ('-date',),
                'default_permissions': ('delete',),
            },
        ),
        migrations.CreateModel(
            name='NotificationReceiver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('email', models.EmailField(verbose_name='e-mail', max_length=254)),
                ('config', models.ForeignKey(related_name='receivers', to='contacts.ContactsConfig')),
            ],
            options={
                'verbose_name': 'notification receiver',
                'verbose_name_plural': 'notification receivers',
            },
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('weekdays', libs.multiselect_field.fields.MultiSelectField(verbose_name='weekdays', max_length=255, choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('start_time', models.TimeField(verbose_name='from', null=True)),
                ('end_time', models.TimeField(verbose_name='to', null=True)),
                ('address', models.ForeignKey(related_name='hours', to='contacts.Address')),
            ],
            options={
                'verbose_name': 'opening hours sequence',
                'verbose_name_plural': 'opening hours sequences',
                'ordering': ('weekdays',),
            },
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.CharField(verbose_name='number', max_length=255, blank=True)),
                ('sort_order', models.PositiveIntegerField(verbose_name='sort order')),
                ('address', models.ForeignKey(related_name='+', to='contacts.Address')),
            ],
            options={
                'verbose_name': 'phone',
                'verbose_name_plural': 'phones',
                'ordering': ('sort_order',),
            },
        ),
    ]
