from django.db import models

class Report(models.Model):
    #created_at = models.DateTimeField(auto_now_add=True)
    company_name=models.CharField(max_length=255)
    company_phone=models.CharField(max_length=255)
    company_location=models.CharField(max_length=255)
    company_country=models.CharField(max_length=255)
    sector=models.CharField(max_length=255)
    industry=models.CharField(max_length=255)
    current_projects=models.TextField()

