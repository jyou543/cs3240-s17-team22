from django import forms
from account.models import User

class MakeGroup(forms.Form):
    name=forms.CharField(label='Group Name:')
    members = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple())
