# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_remove_report_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 10, 16, 0, 34, 53213, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
