# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-16 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MysqlOps', '0015_auto_20190116_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysql_sql_log',
            name='dbname',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
