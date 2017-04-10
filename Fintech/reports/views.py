from django.shortcuts import render
from django.http import HttpResponse
from .models import Report
from django.core.context_processors import csrf
from .forms import ReportForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.views import generic

# view for the index page
class IndexView(generic.ListView):
    # name of the object to be used in the index.html
    context_object_name = 'report_list'
    template_name = 'reports/index.html'

    def get_queryset(self):
        return Report.objects.all()


# view for the new report entry page
class ReportEntry(CreateView):
    model = Report
    # the fields become the entry rows in the generated form
    fields = ['company_name', 'company_phone', 'company_email',
              'company_location', 'company_country', 'sector', 'industry',
              'current_projects', 'private_report', 'files_attached']


class ReportUpdate(UpdateView):
    model = Report
    # the fields become the entry rows in the update form

    fields = ['company_name', 'company_phone', 'company_email',
              'company_location', 'company_country', 'sector', 'industry',
              'current_projects', 'private_report', 'files_attached']


class ReportDelete(DeleteView):
    model = Report
    success_url = reverse_lazy('reports:index')


# def newreport(request):
#     if request.method=='POST':
#
#         # if the report form has been filled out
#         form = ReportForm(request.POST)
#
#         #if all data is valid
#         if form.is_valid():
#             # created_at = request.POST.get["created_at"]
#             company_name = request.POST.get["company_name"]
#             company_phone = request.POST.get["company_phone"]
#             company_email = request.POST.get["company_email"]
#             company_location = request.POST.get["company_location"]
#             company_country = request.POST.get["company_country"]
#             sector = request.POST.get["sector"]
#             industry = request.POST.get["industry"]
#             current_projects = request.POST.get["current_projects"]
#             private_report = request.POST.get["private_report"]
#             files_attached = request.POST.get["files_attached"]
#             report = Report.objects.create(company_name=company_name, company_phone=company_phone,
#                               company_email=company_email, company_location=company_location, company_country=company_country,
#                               sector=sector, industry=industry, current_projects=current_projects, private_report=private_report,
#                               files_attached=files_attached)
#             report.save()
#             reportinfo = ReportForm()
#             reportinfo.save()
#
#             # context = {
#             #     'report_obj': report,
#             #     'is_rendered': True
#             # }
#             return render(request, 'reports/showreportdata.html', )
#
#
#             # redirect after POST
#
#     else:
#             # unbound form
#         form = ReportForm()
#
#     return render(request, 'reports/newreport.html', {'form': form})
#     # else:
#     #     return render(request, 'reports/newreport.html', {'form': form})
#
#
# # functions executes with the showdatareport url to display list of all reports
# def showreportdata(request):
#     all_reports = Report.objects.all()
#     return render(request, 'reports/showreportdata.html', {'all_reports': all_reports})