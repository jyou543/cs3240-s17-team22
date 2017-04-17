from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Report
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import ReportForm
from account.models import CustomUser
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from .models import CustomUser
from django.contrib.auth.models import User



@login_required
def create_report(request):
    if not request.user.is_authenticated():
        return render(request, 'html5up/login.html')
    elif request=='POST':

        form = ReportForm(request.POST)


        if form.is_valid():
            # report = form.save(commit=False)
            created_by = request.CustomUser.user
            company_name = request.POST['company_name']
            company_phone =request.POST['company_phone']
            company_email =request.POST['company_email']
            company_location = request.POST['company_location']
            company_country = request.POST['company_country']
            sector = request.POST['sector']
            industry = request.POST['industry']
            current_projects = request.POST['current_projects']
            private_report = request.POST['private_report']
            files_attached = request.FILES['files_attached']

            report = Report.objects.create(created_by=created_by, company_name=company_name, company_phone=company_phone,
                                           company_email=company_email, company_location=company_location, company_country=company_country,
                                           sector=sector, industry=industry, current_projects=current_projects, private_report=private_report,
                                           files_attached=files_attached)
            report.save()
            return render(request, 'reports:detail', {'report': report})

    else:
        form = ReportForm()

    return render(request, 'reports/report_form.html', {'form': form})



def detail(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    return render(request, 'reports/detail.html', {'report': report})


#
# # view for the index page
# class IndexView(generic.ListView):
#     # name of the object to be used in the index.html
#     context_object_name = 'report_list'
#     template_name = 'reports/index.html'
#
#
#     def get_queryset(self):
#         return Report.objects.all()
#
#
# class DetailView(generic.DetailView):
#     model = Report
#     template_name = 'reports/detail.html'



# # view for the new report entry page
# class ReportCreate(CreateView):
#     model = Report
#     form_class = ReportForm
#     # the fields become the entry rows in the generated form
#     # fields = ['company_name', 'company_phone', 'company_email',
#     #           'company_location', 'company_country', 'sector', 'industry',
#     #           'current_projects', 'private_report', 'files_attached']
#     #
#     # def get_context_data(self, **kwargs):
#     #     context = super(ReportCreate, self).get_context_data(**kwargs)
#     #     context['form'] = ReportForm
#     #     return context
#     #
#     #
#     # def post(self, request, *args, **kwargs):
#     #     # report = Report.objects.get(pk=self.id, default=1)
#     #     form = ReportForm(request.POST)
#     #     return form
#     #
#
#     @login_required
#     def form_valid(self, form):
#         form = ReportForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             report = form.save(commit=False)
#             report.created_by = request.user
#             report.files_attached = request.FILES['files_attached']
#             report.save()
#
#
# class ReportUpdate(UpdateView):
#     model = Report
#     # the fields become the entry rows in the update form
#
#     fields = ['company_name', 'company_phone', 'company_email',
#               'company_location', 'company_country', 'sector', 'industry',
#               'current_projects', 'private_report', 'files_attached']
#
#
# class ReportDelete(DeleteView):
#     model = Report
#     success_url = reverse_lazy('reports:index')
