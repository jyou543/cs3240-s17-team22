from django.conf.urls import include, url
from django.contrib import admin
from account import views as account_views


urlpatterns = [
    # Examples:
    # url(r'^$', 'Fintech.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/', account_views.signupform, name='signup'),
    url(r'^login/', account_views.log),
    url(r'^auth/', account_views.auth),
    url(r'^showdata/', account_views.showdata),
    url(r'^logout/', account_views.logout),
    url(r'^loggedin/', account_views.loggedin),
    url(r'^invalid/', account_views.invalid)

]
