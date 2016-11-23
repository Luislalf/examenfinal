# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actuacion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActuacionVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('codigo', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(7)])),
                ('nombre', models.CharField(max_length=60)),
                ('foto', models.ImageField(upload_to='fotos/')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, default=Decimal('0.00'))),
                ('existencia', models.IntegerField()),
                ('marca', models.ManyToManyField(through='examen.Actuacion', to='examen.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('DPI', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('fecha_venta', models.DateTimeField(default=django.utils.timezone.now)),
                ('DPI', models.ManyToManyField(through='examen.ActuacionVenta', to='examen.Usuario')),
                ('producto', models.ManyToManyField(through='examen.ActuacionVenta', to='examen.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='actuacionventa',
            name='DPI',
            field=models.ForeignKey(to='examen.Usuario'),
        ),
        migrations.AddField(
            model_name='actuacionventa',
            name='producto',
            field=models.ForeignKey(to='examen.Producto'),
        ),
        migrations.AddField(
            model_name='actuacionventa',
            name='venta',
            field=models.ForeignKey(to='examen.Venta'),
        ),
        migrations.AddField(
            model_name='actuacion',
            name='marca',
            field=models.ForeignKey(to='examen.Marca'),
        ),
        migrations.AddField(
            model_name='actuacion',
            name='producto',
            field=models.ForeignKey(to='examen.Producto'),
        ),
    ]
