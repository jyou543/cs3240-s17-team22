from django.db import models
from account.models import CustomUser
from django.contrib.auth.models import Group


class Group(models.Model):
    name=models.CharField(max_length=300)
    members = models.ManyToManyField(CustomUser)
    #group=models.OneToOneField(Group)

    def _str_(self):
        return self.members