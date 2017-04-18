# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customuser_is_sitemanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='private_message',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('body', models.CharField(max_length=300)),
                ('encrypt', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(related_name='receiver', to='account.CustomUser')),
                ('sender', models.ForeignKey(related_name='sender', to='account.CustomUser')),
            ],
        ),
    ]
