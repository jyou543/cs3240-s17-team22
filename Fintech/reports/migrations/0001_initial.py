# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import reports.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20170419_0246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company_name', models.CharField(max_length=255)),
                ('company_phone', models.CharField(max_length=255)),
                ('company_email', models.CharField(max_length=255)),
                ('company_location', models.CharField(max_length=255)),
                ('company_country', models.CharField(max_length=255)),
                ('sector', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=255)),
                ('current_projects', models.TextField()),
                ('private_report', models.BooleanField(default=False)),
                ('files_attached', models.FileField(blank=True, null=True, upload_to=reports.models.content_file_name)),
                ('created_by', models.ForeignKey(to='account.CustomUser', default=1)),
            ],
        ),
    ]
