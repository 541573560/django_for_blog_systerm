# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-02 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gustbook', '0002_auto_20171001_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='words_board',
            name='e_mail',
            field=models.EmailField(default=0, max_length=254),
        ),
    ]
