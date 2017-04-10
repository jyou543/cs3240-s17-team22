from django.db import models
from account.models import User
from django.contrib.auth.models import Group


class Group(models.Model):
    name=models.CharField(max_length=300)
    members = models.ManyToManyField(User)
    #group=models.OneToOneField(Group)
