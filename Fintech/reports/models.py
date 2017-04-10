from django.db import models
from django.core.urlresolvers import reverse


class Report(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True)
    company_name=models.CharField(max_length=255)
    company_phone=models.CharField(max_length=255)
    company_email = models.CharField(max_length=255)
    company_location=models.CharField(max_length=255)
    company_country=models.CharField(max_length=255)
    sector=models.CharField(max_length=255)
    industry=models.CharField(max_length=255)
    current_projects=models.TextField()
    private_report = models.CharField(max_length=100)
    files_attached = models.FileField(blank=True, null=True)

    # returns the name of the company the report is for
    def get_absolute_url(self):
        return reverse('reports:index')

