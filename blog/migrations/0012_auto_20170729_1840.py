# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 10:40
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170729_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='markdown_or_not',
            field=models.CharField(choices=[('m', 'Markdown'), ('c', 'ckeditor')], default='c', max_length=6),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='正文'),
        ),
    ]
