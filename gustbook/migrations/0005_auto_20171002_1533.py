# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-02 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gustbook', '0004_auto_20171002_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words_board',
            name='e_mail',
            field=models.CharField(max_length=52),
        ),
    ]
