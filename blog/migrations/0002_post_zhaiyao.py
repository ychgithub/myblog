# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='zhaiyao',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]