from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User)
    #to store the name of the user
    # username = models.CharField(max_length=100)
    #to store the password of the user
    # email = models.CharField(max_length=100)
    #
    # password = models.CharField(max_length=100)
    type_choice = (
        ("C", "Company User"),
        ('I', "Investor User"),
    )
    user_type = models.CharField(max_length = 1, choices=type_choice, default = 'C')
    # if user_type == 'C':
    #     class Meta:
    #         permissions = (
    #             ("manage_reports", "Can manage reports"),
    #             ("view_reports", "Can View reports"),
    #         )
    # elif user_type == 'I':
    #     class Meta:
    #         permissions = (
    #             ("view_reports", "view reports")
    #         )

#this returns the name of the user when the object of user is printed
    def __str__(self):
        return self.user