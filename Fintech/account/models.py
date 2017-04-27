from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User)
    type_choice = (
        ("C", "Company User"),
        ('I', "Investor User"),
    )
    is_SiteManager = models.BooleanField(default=False)
    user_type = models.CharField(max_length=1, choices=type_choice, default='C')
    publicKey=models.TextField(blank=True)
    privateKey=models.TextField(blank=True)

#this returns the name of the user when the object of user is printed
    def __str__(self):
<<<<<<< HEAD
        sm = "False"
        if self.user.customuser.is_SiteManager:
            sm = "True"
            return self.user.get_username()+ ": " + "Site Manager"
        #return self.user.get_username() + ": " + (self.user.customuser.get_user_type_display()) + sm
        return self.user.get_username() + ": " + (self.user.customuser.get_user_type_display())

=======
        return self.user.get_username() 
>>>>>>> origin/master
