# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planeador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiaplaneada',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='materiaplaneada',
            name='codigo',
            field=models.CharField(max_length=10),
        ),
    ]
