# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-12-28 23:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adquisicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tipo_moneda', models.CharField(choices=[('EUR', 'Euro'), ('CUP', 'Peso Cubano'), ('CUC', 'Peso Cubano Convertible'), ('USD', 'Dolar')], default='CUC', max_length=3)),
                ('tipo_adquisicion', models.CharField(choices=[('CMP', 'Compra'), ('DNC', 'Donación'), ('CNJ', 'Canje')], default='CMP', max_length=3)),
                ('fecha_adquisicion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'managed': True,
                'verbose_name': 'Adquisición',
                'db_table': 'contab_adquisicion',
                'verbose_name_plural': 'Adquisiciones',
            },
        ),
        migrations.CreateModel(
            name='AdqVendedores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_vendedor', models.CharField(default='Teclee el nombre del Vendedor', max_length=50)),
                ('direccion_1', models.TextField(default='Teclee la dirección principal  del vendeddor')),
                ('direccion_2', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion_3', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion_4', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=11, null=True)),
                ('otro_proveedor', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('fax', models.CharField(blank=True, max_length=11, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('descuento', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('es_institucion', models.BooleanField(default=False)),
            ],
            options={
                'managed': True,
                'verbose_name': 'Vendedor',
                'db_table': 'contab_adq_vendedor',
                'verbose_name_plural': 'Vendedores',
            },
        ),
        migrations.CreateModel(
            name='Contratos',
            fields=[
                ('numero_contrato', models.CharField(default='0000000000', max_length=10, primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField(default=django.utils.timezone.now)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(default='Por Favor describa le contrato', max_length=300)),
            ],
            options={
                'managed': True,
                'verbose_name': 'Contrato',
                'db_table': 'contab_contrato',
                'verbose_name_plural': 'Listado de Contratos',
            },
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=4)),
                ('nombre', models.CharField(max_length=40)),
                ('cantidad_aprob', models.DecimalField(decimal_places=2, max_digits=6, max_length=6)),
                ('responsable', models.CharField(default='Teclee el nombre del responsable del Presupuesto ', max_length=40)),
            ],
            options={
                'managed': True,
                'verbose_name': 'Presupuesto',
                'db_table': 'contab_presupuesto',
                'verbose_name_plural': 'Resumen de Presupuestos',
            },
        ),
        migrations.CreateModel(
            name='PresupuestoPeriodo',
            fields=[
                ('id_periodo', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField(default=django.utils.timezone.now)),
                ('fecha_culminacion', models.DateField(default=django.utils.timezone.now)),
                ('periodo', models.DateField(auto_now_add=True, verbose_name='Período de Aprobación del Presupuesto')),
            ],
            options={
                'managed': True,
                'verbose_name': 'Periodo Contable',
                'db_table': 'contab_presupuesto_periodo',
                'verbose_name_plural': 'Resumen de Períodos Contables',
            },
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contabilidad.PresupuestoPeriodo'),
        ),
        migrations.AddField(
            model_name='adquisicion',
            name='nombre_vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contabilidad.AdqVendedores'),
        ),
    ]