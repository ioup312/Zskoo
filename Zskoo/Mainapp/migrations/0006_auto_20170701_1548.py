# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 07:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0005_auto_20170701_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zskoo_conclusion',
            name='main_id',
            field=models.ForeignKey(default='XXX', null=True, on_delete=django.db.models.deletion.CASCADE, to='Mainapp.Zskoo_Main'),
        ),
    ]
