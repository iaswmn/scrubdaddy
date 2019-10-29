# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import libs.storages.media_storage
import libs.file_field.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GetInTouchConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('header', models.CharField(max_length=128, verbose_name='header')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='change date')),
            ],
            options={
                'verbose_name': 'settings',
                'default_permissions': ('change',),
            },
        ),
        migrations.CreateModel(
            name='GetInTouchMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('location', models.CharField(max_length=64, blank=True, verbose_name='Where are you located?')),
                ('phone', models.CharField(max_length=32, blank=True, verbose_name='phone number')),
                ('email', models.EmailField(max_length=254, blank=True, verbose_name='e-mail')),
                ('comments', models.TextField(max_length=2048, verbose_name='your comments')),
                ('reach_type', models.CharField(help_text='Hint: Inquiries are best answered with a quick chat!', choices=[('Phone', 'Phone'), ('Email', 'Email')], verbose_name='How can we reach you?', max_length=128)),
                ('reach_time', models.CharField(max_length=128, verbose_name='Best time to reach you?')),
                ('time_zone', models.CharField(choices=[('ET', 'ET'), ('MT', 'MT'), ('CT', 'CT')], verbose_name='time zone', max_length=128)),
                ('date', models.DateTimeField(editable=False, verbose_name='date sent', default=django.utils.timezone.now)),
                ('referer', models.CharField(editable=False, max_length=512, blank=True, verbose_name='from page')),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
                'default_permissions': ('delete',),
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='GetInTouchMessageImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('file', libs.file_field.fields.ImageField(storage=libs.storages.media_storage.MediaStorage('contacts/images'), verbose_name='image', upload_to='')),
                ('created', models.DateTimeField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('message', models.ForeignKey(to='get_in_touch.GetInTouchMessage', related_name='images')),
            ],
            options={
                'verbose_name': 'get in touch image',
                'verbose_name_plural': 'get in touch images',
                'default_permissions': ('delete',),
                'ordering': ('-created',),
            },
        ),
    ]
