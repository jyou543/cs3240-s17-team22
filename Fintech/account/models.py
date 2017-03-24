from django.db import models


class User(models.Model):
    #to store the name of the user
    username = models.CharField(max_length=100)
    #to store the password of the user
    password = models.CharField(max_length=100)

#this returns the name of the user when the object of user is printed
    def __str__(self):
        return self.username