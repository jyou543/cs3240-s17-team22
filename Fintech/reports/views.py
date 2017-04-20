from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request
from django.utils.decorators import method_decorator

from .models import Report
from django.core.context_processors import csrf, request
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import ReportForm
from account.models import CustomUser
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from .models import CustomUser
from django.contrib.auth.models import User
from django.db.models import Q




# view for the index page
class IndexView(generic.ListView):
    # name of the object to be used in the index.html
    context_object_name = 'report_list'
    template_name = 'reports/index.html'


    def get_queryset(self):
        all_reports=Report.objects.all()
        query = self.request.GET.get('q')
        if query:
            return all_reports.filter(Q(company_name__icontains=query))

        else:
            return Report.objects.all()


# detail view to show all fields for specific form
class DetailView(generic.DetailView):
    model = Report
    template_name = 'reports/detail.html'



# view for the new report entry page
class ReportCreate(CreateView):
    model = Report
    # form_class = ReportForm
    # the fields become the entry rows in the generated form
    fields = ['company_name', 'company_phone', 'company_email',
              'company_location', 'company_country', 'sector', 'industry',
              'current_projects', 'private_report', 'files_attached']


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ReportCreate, self).dispatch(*args, **kwargs)


    def form_valid(self, form):
        obj = form.save(commit=False)
        userC = CustomUser.objects.get(user=self.request.user)
        obj.created_by = userC
        return super(ReportCreate, self).form_valid(form)



class ReportUpdate(UpdateView):
    model = Report
    # the fields become the entry rows in the update form

    fields = ['company_name', 'company_phone', 'company_email',
              'company_location', 'company_country', 'sector', 'industry',
              'current_projects', 'private_report', 'files_attached']


class ReportDelete(DeleteView):
    model = Report
    success_url = reverse_lazy('reports:index')
