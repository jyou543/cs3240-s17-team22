from django.conf.urls import include, url
from django.contrib import admin
from account import views as account_views
from reports import views as reports_views
from groups import views as group_views
from messaging.views import *

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
    url(r'groupHome/$', group_views.groupHome),
    url(r'makeGroups/$', group_views.submit_groups),
    url(r'viewGroups/$', group_views.view_groups),
    url(r'leaveGroups/$', group_views.leave_groups),
    url(r'selectGroupToChange/$', group_views.view_groups_for_adding),
    url(r'selectMembersToAdd/$', group_views.select_members_to_add),
    url(r'addMembers/$', group_views.add_members),
    url(r'invalidSubmitGroup/$', group_views.invalid_submit_group),
    url(r'groupSuccessPage/$', group_views.success),
    url(r'messageHome/$', messageHome),
    url(r'makeMessages/$', new_messages),
    url(r'viewMessages/$', view_messages),
    url(r'deleteMessages/$', delete_messages),
    url(r'invalidSubmitMessage/$', invalid_submit_message),
    url(r'messageSuccessPage/$', success)

]
