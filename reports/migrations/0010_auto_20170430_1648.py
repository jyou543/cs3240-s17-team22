# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_remove_report_files_attached'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyfiles',
            name='company_filename',
        ),
        migrations.RemoveField(
            model_name='investorfiles',
            name='investor_filename',
        ),
    ]
