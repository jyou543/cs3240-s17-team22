# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20170419_0246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company_name', models.CharField(max_length=255)),
                ('ceo_name', models.CharField(max_length=255)),
                ('company_phone', models.CharField(max_length=255)),
                ('company_email', models.CharField(max_length=255)),
                ('company_location', models.CharField(max_length=255)),
                ('company_country', models.CharField(max_length=255)),
                ('sector', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=255)),
                ('current_projects', models.TextField()),
                ('private_report', models.BooleanField(default=False)),
                ('files_attached', models.FileField(upload_to='media/', blank=True, null=True)),
                ('created_by', models.ForeignKey(to='account.CustomUser', default=1)),
            ],
        ),
    ]
