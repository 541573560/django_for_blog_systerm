# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-25 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20171102_1143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '咨询列表'},
        ),
        migrations.AlterModelOptions(
            name='classify',
            options={'verbose_name': '公司名称'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '类别'},
        ),
        migrations.AlterField(
            model_name='classify',
            name='name',
            field=models.CharField(max_length=100, verbose_name='公司名称'),
        ),
    ]
