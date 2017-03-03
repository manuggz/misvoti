# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planeador', '0002_auto_20170228_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiaplaneada',
            name='tipo',
            field=models.CharField(choices=[('RG', 'Regular'), ('EX', 'Extraplan'), ('EL', 'Electiva libre'), ('EA', 'Electiva de Area')], default='RG', max_length=2),
        ),
    ]