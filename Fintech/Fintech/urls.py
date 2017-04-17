from django.conf.urls import include, url
from django.contrib import admin
from account import views as account_views
from reports import views as reports_views
from groups import views as group_views
from messaging.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    #url(r'^$', 'Fintech.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', account_views.home, name='home'),
    url(r'^investor_info/', account_views.investor_info, name='investor_info'),
    url(r'^company_info/', account_views.company_info, name='company_info'),
    url(r'^signup/', account_views.signupform, name='signup'),
    url(r'^login/', account_views.log, name='login'),
    url(r'^auth/', account_views.auth),
    url(r'^showdata/', account_views.showdata),
    url(r'^logout/', account_views.loggedout, name = 'logout'),
    url(r'^loggedin/', account_views.loggedin, name='loggedin'),
    url(r'^invalid/', account_views.invalid),
    url(r'^reports/', include('reports.urls', namespace='reports')),
    url(r'^makeGroups/', group_views.submit_groups),
    url(r'^viewGroups/', group_views.view_groups),
    url(r'^leaveGroups/', group_views.leave_groups),
    url(r'messageHome/$', messageHome),
    url(r'makeMessages/$', new_messages),
    url(r'viewMessages/$', view_messages),
    url(r'deleteMessages/$', delete_messages)

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)