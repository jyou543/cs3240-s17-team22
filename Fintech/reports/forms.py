from django import forms
from .models import Report

class ReportForm(forms.ModelForm):

    files_attached = forms.FileField()

    class Meta:
        model = Report
        fields = ['company_name', 'company_phone', 'company_email',
                  'company_location', 'company_country', 'sector', 'industry',
                  'current_projects', 'private_report', 'files_attached']
        widgets = {"files_attached": forms.FileInput(attrs={'id': 'files', 'required': True, 'multiple': True})}

    # created_at = forms.DateTimeField(label='Created at:')
    # company_name = forms.CharField(label='Company Name:', max_length=255)
    # company_phone = forms.CharField(label='Company Phone:', max_length=255)
    # company_email = forms.CharField(label='Company Email:', max_length=255)
    # company_location = forms.CharField(label='Company Location:', max_length=255)
    # company_country = forms.CharField(label='Company Country:', max_length=255)
    # sector = forms.CharField(label='Sector:',max_length=255)
    # industry = forms.CharField(label='Industry:', max_length=255)
    # current_projects = forms.CharField(widget=forms.Textarea())
    # private_report = forms.TypedChoiceField(coerce=lambda x: x =='True',
    #                                         choices=((False, 'No'), (True, 'Yes')), widget=forms.RadioSelect)
    # files_attached = forms.FileField(label='Files:', widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
