# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pergetlist', '0002_broadcast'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='broadcast',
            name='source',
        ),
        migrations.AddField(
            model_name='source',
            name='broadcast',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='source',
            name='broadcast_end',
            field=models.DateTimeField(default=None, verbose_name='end of broadcast'),
        ),
        migrations.DeleteModel(
            name='Broadcast',
        ),
    ]
