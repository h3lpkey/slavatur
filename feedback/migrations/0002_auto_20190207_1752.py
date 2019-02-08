# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-02-07 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='db_img', verbose_name='изображение')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('credentials', models.CharField(max_length=100, verbose_name='ФИО')),
                ('comment_text', models.TextField(verbose_name='Комментарий')),
            ],
            options={
                'verbose_name_plural': 'Комментарии',
                'verbose_name': 'Комментарий',
            },
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
