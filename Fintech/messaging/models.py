from django.db import models
from account.models import *

class private_message(models.Model):
    sender=models.ForeignKey(CustomUser, related_name="sender")
    recipient=models.ForeignKey(CustomUser, related_name="receiver")
    title=models.CharField(max_length=300)
    body=models.CharField(max_length=300)
    encrypt=models.BooleanField(default=False)

    def _str_(self):
        return self.title
