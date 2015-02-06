# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20150206_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='lines_add',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contribution',
            name='lines_deleted',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
