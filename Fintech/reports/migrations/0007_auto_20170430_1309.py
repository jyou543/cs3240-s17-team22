# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_auto_20170430_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyfiles',
            name='report',
            field=models.ForeignKey(editable=False, to='reports.Report'),
        ),
        migrations.AlterField(
            model_name='investorfiles',
            name='report',
            field=models.ForeignKey(editable=False, to='reports.Report'),
        ),
    ]
