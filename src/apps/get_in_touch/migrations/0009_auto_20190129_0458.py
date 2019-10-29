# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_in_touch', '0008_auto_20190129_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getintouchmessage',
            name='reach_type',
            field=models.CharField(max_length=128, default=('Email', 'Email'), verbose_name='How can we reach you?', choices=[('Phone', 'Phone'), ('Email', 'Email')], help_text='Hint: Inquiries are best answered with a quick chat!'),
        ),
    ]
