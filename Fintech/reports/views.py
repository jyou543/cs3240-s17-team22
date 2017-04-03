from django.shortcuts import render
from .models import Report
from .forms import MakeReport

def submit_report(request):
    if request.method=='POST':
        form = MakeReport(request.POST)
        if form.is_valid():
            #created_at = request.POST.get('created_at','')
            company_name = request.POST.get('company_name','')
            company_phone = request.POST.get('company_phone','')
            company_location = request.POST.get('company_location','')
            company_country = request.POST.get('company_country','')
            sector = request.POST.get('sector','')
            industry = request.POST.get('industry','')
            current_projects = request.POST.get('current_project','')
            report_obj=Report(company_name=company_name, company_phone=company_phone,
                              company_location=company_location, sector=sector, industry=industry, current_projects=current_projects )
            #return render(request, 'newreport.html')
    else:
        form= MakeReport()

    return render(request, 'newreport.html', {'form': form});
