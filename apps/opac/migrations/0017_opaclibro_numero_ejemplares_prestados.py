# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2021-06-30 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opac', '0016_remove_opactesis_cátedra'),
    ]

    operations = [
        migrations.AddField(
            model_name='opaclibro',
            name='numero_ejemplares_prestados',
            field=models.IntegerField(blank=True, default=2, null=True),
        ),
    ]
