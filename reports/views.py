from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, request, HttpResponseForbidden
from django.utils.decorators import method_decorator

from reports.models import Companyfile
from .models import Report
from django.core.context_processors import csrf, request
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import ReportForm, CompanyFilesFormSet, InvestorfileForm, CompanyfileForm
from account.models import CustomUser
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView, FormMixin
from django.views.generic.list import ListView, View
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from .models import CustomUser
from django.contrib.auth.models import User
from django.db.models import Q
from groups.models import Group
from django.forms import inlineformset_factory, ClearableFileInput
from django.db import transaction
from django.forms import formsets
from django.views.decorators.http import require_http_methods

# view for the index page
class IndexView(ListView):
    # name of the object to be used in the index.html
    context_object_name = 'report_list'
    template_name = 'reports/html5up/reports.html'

    # def get_queryset(self):
    #     all_reports=Report.objects.all()
    #     if(not my_user(self.request).is_SiteManager):
    #         all_reports=all_reports.filter(created_by=my_user(self.request))
    #     query = self.request.GET.get('q')
    #     if query:
    #         return all_reports.filter(Q(company_name__icontains=query))
    #
    #     else:
    #         return all_reports

    def get_queryset(self):
        all_reports = Report.objects.all()
        if (not my_user(self.request).is_SiteManager):
            if(all_reports):
                query=Q()
                query |= Q(created_by=my_user(self.request))
                all_groups = Group.objects.all().filter(members=my_user(self.request))
                for group in all_groups:
                    for member in group.members.all():
                        query|=Q(created_by=member)
                query|=Q(private_report=False)
                all_reports=all_reports.filter(query)

        company_name = self.request.GET.get('company_name')
        ceo_name=self.request.GET.get('ceo_name')
        created_at = self.request.GET.get('created_at')
        company_phone = self.request.GET.get('company_phone')
        company_email= self.request.GET.get('company_email')
        company_location= self.request.GET.get('company_location')
        company_sector= self.request.GET.get('company_sector')
        company_industry= self.request.GET.get('company_industry')
        company_projects= self.request.GET.get('company_projects')

        option = self.request.GET.get('option')

        if(option=='and'):
            if (company_name and not company_name==''):
                all_reports=all_reports.filter(company_name__icontains=company_name)
            if (ceo_name and not ceo_name == ''):
                all_reports = all_reports.filter(ceo_name__icontains=ceo_name)
            if (created_at and not created_at==''):
                all_reports=all_reports.filter(created_at__icontains=created_at)
            if (company_phone and not company_phone==''):
                all_reports =all_reports.filter(company_phone__icontains=company_phone)
            if (company_email and not company_email==''):
                all_reports =all_reports.filter(company_email__icontains=company_email)
            if (company_location and not company_location==''):
                all_reports =all_reports.filter(company_location__icontains=company_location)
            if (company_sector and not company_sector==''):
                all_reports =all_reports.filter(sector__icontains=company_sector)
            if (company_industry and not company_industry==''):
                all_reports =all_reports.filter(industry__icontains=company_industry)
            if (company_projects and not company_projects==''):
                all_reports =all_reports.filter(current_projects__icontains=company_projects)
        elif(option=='or'):
            query=Q()
            if(company_name):
                query|=Q(company_name__icontains=company_name)
            if(ceo_name):
                query|=Q(ceo_name__icontains=ceo_name)
            if(created_at):
                query|=Q(created_at__icontains=created_at)
            if(company_phone):
                query|=Q(company_phone__icontains=company_phone)
            if(company_email):
                query|=Q(company_email__icontains=company_email)
            if(company_location):
                query|=Q(company_location__icontains=company_location)
            if(company_sector):
                query|=Q(sector__icontains=company_sector)
            if(company_industry):
                query|=Q(industry__icontains=company_industry)
            if(company_projects):
                query|=Q(current_projects__icontains=company_projects)
            all_reports=all_reports.filter(query)
            # if(not company_name):
            #     company_name=''
            # if(not ceo_name):
            #     ceo_name=None
            # if(not created_at):
            #     created_at=''
            # if(not company_phone):
            #     company_phone=''
            # if(not company_email):
            #     company_email=''
            # if(not company_location):
            #     company_location=''
            # if(not company_sector):
            #     company_sector=''
            # if(not company_industry):
            #     company_industry=''
            # if(not company_projects):
            #     company_projects=''
            # all_reports = all_reports.filter(Q(company_name__icontains=company_name) | Q(ceo_name__icontains=ceo_name) | Q(created_at__icontains=created_at) |
            #                                  Q(company_phone__icontains=company_phone) | Q(company_email__icontains=company_email) | Q(company_location__icontains=company_location) |
            #                                  Q(sector__icontains=company_sector) | Q(industry__icontains=company_industry) | Q(current_projects__icontains=company_projects))


        return all_reports


        # if query:
        #     return all_reports.filter(Q(company_name__icontains=query))
        #
        # else:
        #     return all_reports

def my_user(request):
    user = None
    if request.user.is_authenticated():
        user = request.user
        # return username
    return CustomUser.objects.all().filter(user=user)[0]
    #     return CustomUser.objects.all()


# detail view to show all fields for specific form
class ReportDetailView(FormMixin, DetailView):
    model = Report
    template_name = 'reports/detail.html'
    # if CustomUser.objects.get(user=self.request.user):
    form_class = CompanyfileForm
    # else:
    # form_class = InvestorfileForm

    def get_form_class(self):
        # if request.user.is_authenticated():
        user = CustomUser.objects.get(user=self.request.user)
        userType = user.user_type
        if userType == 'I':
            return InvestorfileForm
        else:
            return CompanyfileForm



    def get_success_url(self):
        return reverse('reports:detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(ReportDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        return super(ReportDetailView, self).form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super(ReportCreate, self).get_context_data(**kwargs)
    #     context['form'] = CompanyfileCreate
    #     return context
    #
    # # @require_http_methods(["POST"])
    # def post(self, request, *args, **kwargs):
    #     return CompanyfileCreate.post(self, request, *args, **kwargs)



class CompanyfileCreate(FormView):
    model = Companyfile
    form_class = CompanyfileForm
    template_name = 'reports/companyfile_form.html'
    success_url = reverse_lazy('reports:index')

    def form_valid(self, form):
        # form.ReportCreate()
        return super().form_valid(form)








# view for the new report entry page
class ReportCreate(FormView):
    model = Report
    form_class = ReportForm
    # object = None
    template_name = 'reports/report_form.html'
    # success_url =
    # success_url = 'reports/detail.hmtl'
#     # the fields become the entry rows in the generated form
#     fields = ['company_name', 'ceo_name', 'company_phone', 'company_email',
#               'company_location', 'company_country', 'sector', 'industry',
#               'current_projects', 'private_report']     #, 'files_attached']
#
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(ReportCreate, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(ReportCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['companyfiles'] = CompanyFilesFormSet(self.request.POST)
            # context['investorfiles_form'] = InvestorFilesFormSet(self.request.POST, self.request.FILES)
        else:
            context['companyfiles'] = CompanyFilesFormSet()
            # context['investorfiles_form'] = InvestorFilesFormSet()
        return context


    def form_valid(self, form):
        context = self.get_context_data()
        companyfiles = context['companyfiles']

        if form.is_valid():
            self.object = form.save(commit=False)
            userC = CustomUser.objects.get(user=self.request.user)
            self.object.created_by = userC
            self.object = form.save()
        if companyfiles.is_valid():
            companyfiles.instance = self.object
            companyfiles.save(commit=False)
            obj_report = form.instance
            boolen_value = self.request.POST.get('companyfile_set-0-encrypted')
            if boolen_value == 'on':
                a = bool('true')
            else:
                a = bool('')
            for cf in self.request.FILES.getlist('companyfile_set-0-cfile'):
                Companyfile.objects.create(report=obj_report,
                                           cfile=cf,
                                           encrypted=a
                                           )




        # obj = form.save(commit=False)
        #
        # obj.created_by = userC
        return super(ReportCreate, self).form_valid(form)


    def get_success_url(self):
        return reverse_lazy('reports:index')

#
#

# def manage_companyfiles(request, report_id):
#     report = Report.objects.get(pk=report_id)
#     CompanyFilesFormSet = inlineformset_factory(Report, CompanyFiles, fields=('company_file', 'encrypted'),
#                                                 widgets={'company_file': ClearableFileInput(
#                                                     attrs={'id': 'files', 'required': False, 'multiple': True})})
#     if request.method == 'POST':
#         formset = CompanyFilesFormSet(request.POST, request.FILES, instance=report)
#         if formset.is_valid():
#             formset.save()
#             return HttpResponseRedirect(report.get_absolute_url())
#         else:
#             formset = CompanyFilesFormSet(instance=report)
#         return render_to_response("reports/report_form.html", {
#             "formset": formset,
#         })




class ReportUpdate(UpdateView):
    model = Report
    # the fields become the entry rows in the update form

    fields = ['company_name', 'ceo_name', 'company_phone', 'company_email',
              'company_location', 'company_country', 'sector', 'industry',
              'current_projects', 'private_report', ]
    # form_class = ReportForm
    print("tger")
    success_url = reverse_lazy('reports:index')

class ReportDelete(DeleteView):
    model = Report
    success_url = reverse_lazy('reports:index')




