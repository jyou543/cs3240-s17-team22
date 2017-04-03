from django import forms

class MakeReport(forms.Form):
    #created_at = forms.DateTimeField(auto_now_add=True)
    company_name = forms.CharField(label='Company Name:', max_length=255)
    company_phone = forms.CharField(label='Company Phone:', max_length=255)
    company_location = forms.CharField(label='Company Location:', max_length=255)
    company_country = forms.CharField(label='Company Country:', max_length=255)
    sector = forms.CharField(label='Sector:',max_length=255)
    industry = forms.CharField(label='Industry:', max_length=255)
    current_projects = forms.CharField(widget=forms.Textarea())
    files = forms.FileField(label='Files:', widget=forms.ClearableFileInput(attrs={'multiple': True}))
