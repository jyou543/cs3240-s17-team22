# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_report_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='created_at',
        ),
    ]
