# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2021-06-30 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_usuarios_biblioteca', '0002_registrousuarios_prestamo_excepcional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrousuarios',
            name='nombre_apellidos',
            field=models.CharField(default=' ', max_length=90),
        ),
    ]
