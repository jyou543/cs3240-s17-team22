# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20170430_0337'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyFiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c_filename', models.CharField(max_length=100)),
                ('c_file', models.FileField(null=True, upload_to=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvestorFiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('i_filename', models.CharField(max_length=100)),
                ('i_file', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.RemoveField(
            model_name='report',
            name='files_attached',
        ),
        migrations.AddField(
            model_name='investorfiles',
            name='report',
            field=models.ForeignKey(to='reports.Report'),
        ),
        migrations.AddField(
            model_name='companyfiles',
            name='report',
            field=models.ForeignKey(to='reports.Report'),
        ),
    ]
