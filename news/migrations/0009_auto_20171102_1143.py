# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-02 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20171031_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='news.Tag'),
        ),
    ]