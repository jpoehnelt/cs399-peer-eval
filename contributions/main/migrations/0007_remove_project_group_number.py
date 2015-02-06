# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_project_commits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='group_number',
        ),
    ]
