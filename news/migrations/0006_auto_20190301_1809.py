# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-03-01 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20190219_0112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image_present',
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотография для новости'),
        ),
    ]
