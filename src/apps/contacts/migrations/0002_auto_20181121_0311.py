# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getintouchmessage',
            name='comments',
            field=models.TextField(max_length=2048, verbose_name='your comments'),
        ),
        migrations.AlterField(
            model_name='getintouchmessage',
            name='phone',
            field=models.CharField(max_length=32, verbose_name='phone number', blank=True),
        ),
        migrations.AlterField(
            model_name='getintouchmessage',
            name='reach_time',
            field=models.CharField(max_length=128, verbose_name='Best time to reach you?'),
        ),
        migrations.AlterField(
            model_name='getintouchmessage',
            name='reach_type',
            field=models.CharField(max_length=128, choices=[('Phone', 'Phone'), ('Email', 'Email')], verbose_name='How can we reach you?', help_text='Hint: Inquiries are best answered with a quick chat!'),
        ),
    ]
