# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20150206_2109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contribution',
            old_name='lines_add',
            new_name='lines_added',
        ),
    ]
