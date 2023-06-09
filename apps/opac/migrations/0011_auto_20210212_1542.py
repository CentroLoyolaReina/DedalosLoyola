# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2021-02-12 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opac', '0010_auto_20210212_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opacrevsarticulo',
            name='autor2',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='autor_secundario', to='opac.OpacAutor'),
        ),
        migrations.AlterField(
            model_name='opacrevsarticulo',
            name='autor3',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='autor_tercero', to='opac.OpacAutor'),
        ),
        migrations.AlterField(
            model_name='opacrevsarticulo',
            name='autor4',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='autor_cuarto', to='opac.OpacAutor'),
        ),
    ]
