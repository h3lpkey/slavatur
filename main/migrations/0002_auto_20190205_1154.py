# Generated by Django 2.1.5 on 2019-02-05 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modules',
            name='order',
        ),
        migrations.RemoveField(
            model_name='modules',
            name='publication',
        ),
    ]
