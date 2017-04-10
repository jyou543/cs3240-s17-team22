from django.conf.urls import url
from . import views

app_name = 'reports'

urlpatterns = [

    # /modelforms/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # modelforms/product/entry
    url(r'^report/entry/$', views.ReportEntry.as_view(), name='report-entry'),

    # modelforms/product/2
    url(r'^report/(?P<pk>[0-9]+)/$', views.ReportUpdate.as_view(), name='report-update'),

    # modelforms/product/(?P<pk>[0-9]+)/delete
    url(r'^report/(?P<pk>[0-9]+)/delete$', views.ReportDelete.as_view(), name='report-delete'),

    # # /users/signup:url to take the input from the user
    # url(r'^newreport/$', views.newreport, name='newreport'),
    # # /users/showdata:url to display the list of users stored on the database
    # url(r'^showreportdata$', views.showreportdata, name='showreportdata'),
]