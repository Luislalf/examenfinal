# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examen', '0002_auto_20161122_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actuacionventa',
            name='DPI',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='DPI',
        ),
        migrations.AddField(
            model_name='venta',
            name='DPI',
            field=models.ForeignKey(default=1, to='examen.Usuario'),
            preserve_default=False,
        ),
    ]
