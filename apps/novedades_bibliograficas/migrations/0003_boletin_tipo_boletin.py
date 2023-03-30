# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2021-02-05 00:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novedades_bibliograficas', '0002_tipoboletin'),
    ]

    operations = [
        migrations.AddField(
            model_name='boletin',
            name='tipo_boletin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='novedades_bibliograficas.TipoBoletin'),
        ),
    ]