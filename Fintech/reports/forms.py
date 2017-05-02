from django import forms
from .models import Report, Investorfile, Companyfile
from django.forms.models import inlineformset_factory



class ReportForm(forms.ModelForm):

    # files_attached = forms.FileField()

    class Meta:
        model = Report
        fields = ('company_name', 'company_phone', 'company_email',
                  'company_location', 'company_country', 'sector', 'industry',
                  'current_projects', 'private_report')


class CompanyfileForm(forms.ModelForm):

    class Meta:
        model = Companyfile
        fields = ('cfile', 'encrypted')
        widgets = {'cfile': forms.ClearableFileInput(attrs={'id': 'files', 'required': False, 'multiple': True})}
#
#
class InvestorfileForm(forms.ModelForm):

    class Meta:
        model = Investorfile
        fields = ['ifile', 'encrypted']
        widgets = {'ifile': forms.ClearableFileInput(attrs={'id': 'files', 'required': False, 'multiple': True})}


# class CompanyFilesForm(forms.ModelForm):
#
#     class Meta:
#         model = CompanyFiles
#         fields = ['company_file', 'encrypted']
#         widgets = {'company_file': forms.ClearableFileInput(attrs={'id': 'files', 'required': False, 'multiple': True})}
#
#
# class InvestorFilesForm(forms.ModelForm):
#
#     class Meta:
#         model = InvestorFiles
#         fields = ['investor_file', 'encrypted']
#         widgets = {'investor_file': forms.ClearableFileInput(attrs={'id': 'files', 'required': False, 'multiple': True})}

# ReportFormSet = modelformset_factory(Report, form=ReportForm)
CompanyFilesFormSet = inlineformset_factory(Report, Companyfile, form=CompanyfileForm, extra=1)

InvestorFilesFormSet = inlineformset_factory(Report, Investorfile, form=InvestorfileForm, extra=1)
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
