# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150206_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='username',
            new_name='github_username',
        ),
    ]
