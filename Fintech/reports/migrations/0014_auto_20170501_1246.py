# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import reports.models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0013_auto_20170430_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companyfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cfile', models.FileField(null=True, upload_to=reports.models.content_file_name, blank=True)),
                ('encrypted', models.BooleanField(default=False)),
                ('report', models.ForeignKey(editable=False, to='reports.Report')),
            ],
        ),
        migrations.CreateModel(
            name='Investorfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ifile', models.FileField(null=True, upload_to=reports.models.content_file_name, blank=True)),
                ('encrypted', models.BooleanField(default=False)),
                ('report', models.ForeignKey(editable=False, to='reports.Report')),
            ],
        ),
        migrations.RemoveField(
            model_name='companyfiles',
            name='report',
        ),
        migrations.RemoveField(
            model_name='investorfiles',
            name='report',
        ),
        migrations.DeleteModel(
            name='CompanyFiles',
        ),
        migrations.DeleteModel(
            name='InvestorFiles',
        ),
    ]
