# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20170403_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='private_message',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('body', models.CharField(max_length=300)),
                ('recipient', models.ForeignKey(to='account.CustomUser', related_name='receiver')),
                ('sender', models.ForeignKey(to='account.CustomUser', related_name='sender')),
            ],
        ),
    ]
