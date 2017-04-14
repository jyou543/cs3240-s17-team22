from django import forms


def check_recipient(recipient):
    if recipient.is_authenticated():
        return None


class NewMessageForm(forms.Form):
    #check_recipient(recipient)
    #recipient=forms.RegexField(regex=r'^\w+$', label='Send To ', error_message='No user')
    recipient=forms.CharField(label='Send To')
    title = forms.CharField(label='Title of Message:')
    body=forms.CharField(label='Body of Message', widget=forms.Textarea())
    #encrypt=forms.BooleanField(widget=forms.CheckboxInput(), required=False, label='Encrypted?')



