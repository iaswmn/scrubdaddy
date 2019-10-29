# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('network', models.CharField(verbose_name='social network', max_length=32, default='facebook', choices=[('facebook', 'Facebook'), ('twitter', 'Twitter'), ('google', 'Google Plus'), ('linkedin', 'Linked In')])),
                ('text', models.TextField(verbose_name='text')),
                ('url', models.URLField(verbose_name='URL')),
                ('scheduled', models.BooleanField(verbose_name='sheduled to share', default=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True, editable=False)),
                ('created', models.DateTimeField(verbose_name='created on', default=django.utils.timezone.now, editable=False)),
                ('posted', models.DateTimeField(verbose_name='posted on', null=True, editable=False)),
                ('content_type', models.ForeignKey(blank=True, null=True, editable=False, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'feed post',
                'verbose_name_plural': 'feeds',
                'ordering': ('-scheduled', '-created'),
            },
        ),
        migrations.CreateModel(
            name='SocialConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('google_apikey', models.CharField(verbose_name='API Key', max_length=48, blank=True, default='AIzaSyB4CphiSoXhku-rP9m5-QkXE9U11OJkOzg')),
                ('twitter_client_id', models.CharField(verbose_name='API Key', max_length=48, blank=True)),
                ('twitter_client_secret', models.CharField(verbose_name='API Secret', max_length=64, blank=True)),
                ('twitter_access_token', models.CharField(verbose_name='Access Token', max_length=64, blank=True)),
                ('twitter_access_token_secret', models.CharField(verbose_name='Access Token Secret', max_length=64, blank=True)),
                ('facebook_client_id', models.CharField(verbose_name='App ID', max_length=48, blank=True)),
                ('facebook_client_secret', models.CharField(verbose_name='App Secret', max_length=64, blank=True)),
                ('facebook_access_token', models.TextField(verbose_name='Access Token', blank=True)),
                ('linkedin_client_id', models.CharField(verbose_name='API Key', max_length=48, blank=True)),
                ('linkedin_client_secret', models.CharField(verbose_name='API Secret', max_length=48, blank=True)),
                ('linkedin_access_token', models.TextField(verbose_name='Access Token', blank=True)),
                ('instagram_client_id', models.CharField(verbose_name='Client ID', max_length=48, blank=True)),
                ('instagram_client_secret', models.CharField(verbose_name='Client Secret', max_length=48, blank=True)),
                ('instagram_access_token', models.CharField(verbose_name='Access Token', max_length=64, blank=True)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'Settings',
                'default_permissions': ('change',),
            },
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('social_google', models.URLField(verbose_name='google plus', max_length=255, blank=True)),
                ('social_twitter', models.URLField(verbose_name='twitter', max_length=255, blank=True)),
                ('social_facebook', models.URLField(verbose_name='facebook', max_length=255, blank=True)),
                ('social_instagram', models.URLField(verbose_name='instagram', max_length=255, blank=True)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
            ],
            options={
                'verbose_name': 'Links',
                'default_permissions': ('change',),
            },
        ),
        migrations.AlterIndexTogether(
            name='feedpost',
            index_together=set([('network', 'content_type', 'object_id')]),
        ),
    ]
