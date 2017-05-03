from django import forms
from .models import Report, Investorfile, Companyfile
from django.forms.models import inlineformset_factory, BaseInlineFormSet



class ReportForm(forms.ModelForm):

    # files_attached = forms.FileField()

    class Meta:
        model = Report
        fields = ['company_name', 'ceo_name', 'company_phone', 'company_email',
                  'company_location', 'company_country', 'sector', 'industry',
                  'current_projects', 'private_report']


class CompanyfileForm(forms.ModelForm):

    class Meta:
        model = Companyfile
        fields =['cfile', 'encrypted']
        widgets = {'cfile': forms.ClearableFileInput(attrs={'id': 'files', 'required': False, 'multiple': False})}
#
#
class InvestorfileForm(forms.ModelForm):

    class Meta:
        model = Investorfile
        fields = ['ifile', 'encrypted']
        widgets = {'ifile': forms.ClearableFileInput(attrs={'id': 'files', 'required': False, 'multiple': False})}





CompanyFilesFormSet = inlineformset_factory(Report, Companyfile, form=CompanyfileForm, extra=1)

InvestorFilesFormSet = inlineformset_factory(Report, Investorfile, form=InvestorfileForm, extra=1)

