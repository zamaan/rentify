# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-27 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id_proof',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]
