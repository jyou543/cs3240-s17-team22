# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customuser_is_sitemanager'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='privateKey',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='publicKey',
            field=models.TextField(blank=True),
        ),
    ]
