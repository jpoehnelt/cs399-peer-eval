# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150206_2059'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contribution',
            unique_together=set([('student', 'project')]),
        ),
    ]
