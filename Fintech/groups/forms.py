from django import forms
from account.models import CustomUser

class MakeGroup(forms.Form):
    name = forms.CharField(label='Group Name:')
    allUsers = CustomUser.objects.all()
    # allUsers.exclude(user=self.user)
    #members = forms.ModelMultipleChoiceField(queryset=CustomUser.objects.all(), widget=forms.CheckboxSelectMultiple())
    members = forms.ModelMultipleChoiceField(queryset=allUsers, widget=forms.CheckboxSelectMultiple())

    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('current_user', None)
    #     super(MakeGroup, self).__init__(*args, **kwargs)  # Make sure to change "YourForm" to your form's class name
    #     self.fields['allUser'].exclude(user=self.user)
