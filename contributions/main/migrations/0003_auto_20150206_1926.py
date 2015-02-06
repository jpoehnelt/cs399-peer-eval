# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_project_date_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='group_number',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='commits',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
