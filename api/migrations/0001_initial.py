# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 08:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
