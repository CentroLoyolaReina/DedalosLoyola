# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2021-06-30 22:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opac', '0013_auto_20210630_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opaclibro',
            old_name='casa_editora',
            new_name='editorial',
        ),
    ]