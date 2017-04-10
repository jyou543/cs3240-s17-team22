# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_report_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='files_attached',
            field=models.FileField(null=True, upload_to='', blank=True),
        ),
    ]
