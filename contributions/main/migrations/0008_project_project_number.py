# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_project_group_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_number',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
