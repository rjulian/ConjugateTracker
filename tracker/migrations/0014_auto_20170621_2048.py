# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-22 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0013_auto_20170621_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deadliftmovement',
            name='chain_weight',
            field=models.IntegerField(blank=True),
        ),
    ]
