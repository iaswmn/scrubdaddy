# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20181122_0542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('text', models.TextField(verbose_name='text')),
                ('position', models.CharField(verbose_name='position', choices=[('top-left', 'top left'), ('top-center', 'top center'), ('top-right', 'top right'), ('right', 'right'), ('bottom-right', 'bottom right'), ('bottom-center', 'bottom center'), ('bottom-left', 'bottom left'), ('left', 'left')], max_length=64)),
                ('event', models.ForeignKey(verbose_name='hint', to='about.Event', related_name='hints')),
            ],
            options={
                'verbose_name': 'hint',
                'verbose_name_plural': 'hints',
            },
        ),
    ]
