from django.conf.urls import url
# from .views import IndexView, DetailView, ReportUpdate, ReportCreate, ReportDelete
from . import views

app_name = 'reports'

urlpatterns = [

    # /modelforms/
    # url(r'^$', IndexView.as_view(), name='index'),

    url(r'^(?P<report_id>[0-9]+)/$', views.detail, name='detail'),

    # modelforms/product/entry
    url(r'^create_report/$', views.create_report, name='create_report'),

    # # modelforms/product/2
    # url(r'^report/(?P<pk>[0-9]+)/$/$', ReportUpdate.as_view(), name='report-update'),
    #
    # # modelforms/product/(?P<pk>[0-9]+)/delete
    # url(r'^report/(?P<pk>[0-9]+)/delete$', ReportDelete.as_view(), name='report-delete'),

    # # /users/signup:url to take the input from the user
    # url(r'^newreport/$', views.newreport, name='newreport'),
    # # /users/showdata:url to display the list of users stored on the database
    # url(r'^showreportdata$', views.showreportdata, name='showreportdata'),
]