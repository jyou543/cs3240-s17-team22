# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20170430_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorfiles',
            name='investor_file',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
