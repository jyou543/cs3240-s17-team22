#importing forms
from django import forms
from .models import CustomUser
#creating our forms


class SignupForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('user_type',)