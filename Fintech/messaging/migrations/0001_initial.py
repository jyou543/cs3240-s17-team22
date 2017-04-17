# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='private_message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('body', models.CharField(max_length=300)),
                ('recipient', models.ForeignKey(to='account.CustomUser', related_name='receiver')),
                ('sender', models.ForeignKey(to='account.CustomUser', related_name='sender')),
            ],
        ),
    ]
