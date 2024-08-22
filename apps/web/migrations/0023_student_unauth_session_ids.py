# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-09 21:02
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_increase_period_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='unauth_session_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32, unique=True), default=[], size=None),
        ),
    ]
