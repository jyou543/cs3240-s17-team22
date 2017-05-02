# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20170430_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='files_attached',
            field=models.FileField(null=True, upload_to=b'uploads/', blank=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='created_by',
            field=models.ForeignKey(default=1, editable=False, to='account.CustomUser'),
        ),
    ]
