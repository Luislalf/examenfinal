# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examen', '0003_auto_20161122_2038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='producto',
            new_name='productos',
        ),
    ]
