# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pergetlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=2048)),
                ('enddate', models.DateTimeField(verbose_name='End date')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pergetlist.Source')),
            ],
        ),
    ]
