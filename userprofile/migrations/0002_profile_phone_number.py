# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-26 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default=91, max_length=100),
            preserve_default=False,
        ),
    ]
