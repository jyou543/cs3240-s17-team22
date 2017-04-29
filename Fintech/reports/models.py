from django.db import models
from django.core.urlresolvers import reverse
from account.models import CustomUser
from django.contrib.auth.models import User




def content_file_name(instance, filename):
    return '/'.join(['report', str(instance.created_by), filename])



class Report(models.Model):
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    company_name=models.CharField(max_length=255)
    ceo_name=models.CharField(max_length=255)
    company_phone=models.CharField(max_length=255)
    company_email = models.CharField(max_length=255)
    company_location=models.CharField(max_length=255)
    company_country=models.CharField(max_length=255)
    sector=models.CharField(max_length=255)
    industry=models.CharField(max_length=255)
    current_projects=models.TextField()
    private_report = models.BooleanField(default=False)
    #files_attached = models.FileField(blank=True, null=True, upload_to=content_file_name)
    files_attached = models.FileField(blank=True, null=True, upload_to="uploads/")


    # returns the name of the company the report is for
    def get_absolute_url(self):
        return reverse('reports:index')#, kwargs={'pk': self.pk})
