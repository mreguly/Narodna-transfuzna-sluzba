# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-10 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isnts', '0003_auto_20170106_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='additional_info',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='employee_additional_info',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
