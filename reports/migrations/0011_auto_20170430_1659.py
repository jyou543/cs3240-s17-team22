# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0010_auto_20170430_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyfiles',
            name='company_filename',
            field=models.CharField(default=datetime.datetime(2017, 4, 30, 20, 59, 7, 198658, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='investorfiles',
            name='investor_filename',
            field=models.CharField(default=datetime.datetime(2017, 4, 30, 20, 59, 12, 896107, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
