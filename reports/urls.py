from django.conf.urls import url
from .views import IndexView, ReportDetailView, ReportUpdate, ReportCreate, ReportDelete, CompanyfileCreate, addFile
# from . import views
from django.conf.urls.static import static
from django.middleware.http import ConditionalGetMiddleware
from django.views.generic import RedirectView


app_name = 'reports'

urlpatterns = [

    # /modelforms/
    url(r'^$', IndexView.as_view(), name='index'),

    url(r'^(?P<pk>[0-9]+)/$', ReportDetailView.as_view(), name='detail'),

    # modelforms/product/entry
    url(r'^report/add/$', ReportCreate.as_view(), name='report-add'),

    url(r'^companyfile/$', CompanyfileCreate.as_view(), name='companyfile_form'),

    # modelforms/product/2
    url(r'^report/(?P<pk>[0-9]+)/$', ReportUpdate.as_view(), name='report-update'),

    url(r'^(?P<pk>[0-9]+)/addfiles/$', addFile),
    # url(r'/addfiles/$', addFile),



    # modelforms/product/(?P<pk>[0-9]+)/delete
    url(r'^report/(?P<pk>[0-9]+)/delete/$', ReportDelete.as_view(), name='report-delete'),

    # # /users/signup:url to take the input from the user
    # url(r'^newreport/$', views.newreport, name='newreport'),
    # # /users/showdata:url to display the list of users stored on the database
    # url(r'^showreportdata$', views.showreportdata, name='showreportdata'),
]