from django import forms
from account.models import CustomUser

class MakeGroup(forms.Form):
    name=forms.CharField(label='Group Name:')
    members = forms.ModelMultipleChoiceField(queryset=CustomUser.objects.all(), widget=forms.CheckboxSelectMultiple())
