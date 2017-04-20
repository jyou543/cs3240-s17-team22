from django import forms
from account.models import CustomUser

class MakeGroup(forms.Form):
    name = forms.CharField(label='Group Name:')
    # allUsers.exclude(user=self.user)
    #members = forms.ModelMultipleChoiceField(queryset=CustomUser.objects.all(), widget=forms.CheckboxSelectMultiple())

    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user', None)
        super(MakeGroup, self).__init__(*args, **kwargs)  # Make sure to change "YourForm" to your form's class name
        users = CustomUser.objects.exclude(user=current_user)
        self.fields['members']=forms.ModelMultipleChoiceField(queryset=users,widget=forms.CheckboxSelectMultiple())

