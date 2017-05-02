# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20170430_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyfiles',
            name='encrypted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='investorfiles',
            name='encrypted',
            field=models.BooleanField(default=False),
        ),
    ]
