from django.conf.urls import patterns, include, url
from django.contrib import admin
from table_query_app.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'katalogen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^update/$', import_db),

    url(r'^$', 'login_app.views.index', name='login_home'),
    url(r'^medlemmar/$', 'homeview_app.views.get_members', name='members'),
    url(r'^medlem/$', 'table_query_app.views.get_member_info', name='member_info'),
    url(r'^namn/$', 'table_query_app.views.get_member_name', name='member_name'),
    url(r'^auth/$', 'login_app.views.login_from_link', name='login_from_link'),
    url(r'^login/$', 'login_app.views.login_attempt', name='login_attempt'),
    url(r'^logout/$', 'login_app.views.logout_user', name='logout_user'),
    url(r'^search/', 'homeview_app.views.search', name='search'),
)
