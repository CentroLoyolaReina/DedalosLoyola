# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2021-06-30 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opac', '0012_auto_20210630_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opaclibro',
            name='año_de_edición',
            field=models.CharField(blank=True, default='', max_length=9, null=True),
        ),
    ]
