# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20170419_0246'),
    ]

    operations = [
        migrations.CreateModel(
            name='private_message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('body', models.CharField(max_length=1000)),
                ('encrypt', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(to='account.CustomUser', related_name='receiver')),
                ('sender', models.ForeignKey(to='account.CustomUser', related_name='sender')),
            ],
        ),
    ]
