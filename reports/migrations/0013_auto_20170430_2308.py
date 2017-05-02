# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0012_auto_20170430_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyfiles',
            name='company_file',
            field=models.FileField(null=True, upload_to=b'uploads/', blank=True),
        ),
        migrations.AlterField(
            model_name='investorfiles',
            name='investor_file',
            field=models.FileField(null=True, upload_to=b'uploads/', blank=True),
        ),
    ]
