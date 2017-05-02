# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_auto_20170430_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='files_attached',
        ),
    ]
