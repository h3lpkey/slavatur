# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-02-27 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_auto_20190227_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотография для отзыва'),
        ),
    ]
