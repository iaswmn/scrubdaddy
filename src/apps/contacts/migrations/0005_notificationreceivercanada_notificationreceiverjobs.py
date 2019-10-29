# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_phonenumber_phone_word'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationReceiverCanada',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('config', models.ForeignKey(to='contacts.ContactsConfig', related_name='receivers_canada')),
            ],
            options={
                'verbose_name': 'notification receiver Canada',
                'verbose_name_plural': 'notification receivers Canada',
            },
        ),
        migrations.CreateModel(
            name='NotificationReceiverJobs',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('config', models.ForeignKey(to='contacts.ContactsConfig', related_name='receivers_jobs')),
            ],
            options={
                'verbose_name': 'notification receiver jobs',
                'verbose_name_plural': 'notification receivers jobs',
            },
        ),
    ]
