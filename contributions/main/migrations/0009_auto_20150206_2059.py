# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_project_project_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='github_username',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
