from django.conf.urls import include, url
from django.contrib import admin
from account import views as account_views
# from reports import views as reports_views
from groups import views as group_views
from messaging.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
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
    url(r'groups/$', group_views.groupHome, name = 'groups'),
    url(r'makeGroups/$', group_views.submit_groups, name = 'makeGroups'),
    url(r'viewGroups/$', group_views.view_groups, name = 'viewGroups'),
    url(r'leaveGroups/$', group_views.leave_groups),
    url(r'selectGroupToChange/$', group_views.view_groups_for_adding, name= 'selectGroup'),
    url(r'selectMembersToAdd/$', group_views.select_members_to_add, name = 'selectMembers'),
    url(r'addMembers/$', group_views.add_members, name = 'addMembers'),
    url(r'invalidSubmitGroup/$', group_views.invalid_submit_group),
    url(r'groupSuccessPage/$', group_views.success),

    #SITE MANAGER GROUP URLS
    url(r'groupHomeSiteManager/$', group_views.groupHomeSiteManager, name = 'groupHomeSiteManager'),
    url(r'deleteGroupsSiteManager/$', group_views.delete_groups_site_manager),
    url(r'viewGroupsSiteManager/$', group_views.view_groups_site_manager, name = 'viewGroupsSiteManager'),
    url(r'selectGroupToAddMembersSiteManager/$', group_views.view_groups_for_adding_site_manager, name = 'selectGroupToAddMembersSiteManager'),
    url(r'selectMembersToAddSiteManager/$', group_views.select_members_to_add_site_manager),
    url(r'addMembersSiteManager/$', group_views.add_members_site_manager, name = 'addMembersSiteManager'),
    url(r'selectGroupToDeleteMembersSiteManager/$', group_views.view_groups_for_deleting_site_manager, name = 'selectGroupToDeleteMembersSiteManager'),
    url(r'selectMembersToDeleteSiteManager/$', group_views.select_members_to_delete_site_manager),
    url(r'deleteMembersSiteManager/$', group_views.delete_members_site_manager),
    url(r'revokeSm/$', account_views.revoke_sm),
    url(r'suspendUser/$', account_views.sus_user),
    url(r'makeSiteManager/$', account_views.make_sm),

    url(r'messageHome/$', messageHome, name= 'messaging'),
    url(r'makeMessages/$', new_messages, name = 'makeMessages'),
    url(r'makeGroupMessages/$', message_groups, name = 'makeGroupMessages'),
    url(r'viewMessages/$', view_messages, name = 'viewMessages'),
    url(r'deleteMessages/$', delete_messages),
    url(r'invalidSubmitMessage/$', invalid_submit_message),
    url(r'messageSuccessPage/$', success),
    # url(r'enterPrivateKey/$', enter_password),
    url(r'decryptMessages/$', decrypt_messages),
    url(r'^fdaLogin/$', account_views.fdalogin),
    url(r'^viewReports/$', account_views.view_reports),
    url(r'^viewOne/$', account_views.view_one),
    url(r'^getEncrypt/$', account_views.get_encrypt),
    url(r'^$', account_views.index)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)