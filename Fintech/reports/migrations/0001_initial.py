# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import reports.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
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
                ('files_attached', models.FileField(null=True, upload_to=reports.models.content_file_name, blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
