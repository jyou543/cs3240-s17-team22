# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20170430_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyfiles',
            old_name='c_file',
            new_name='company_file',
        ),
        migrations.RenameField(
            model_name='companyfiles',
            old_name='c_filename',
            new_name='company_filename',
        ),
        migrations.RenameField(
            model_name='investorfiles',
            old_name='i_file',
            new_name='investor_file',
        ),
        migrations.RenameField(
            model_name='investorfiles',
            old_name='i_filename',
            new_name='investor_filename',
        ),
    ]
