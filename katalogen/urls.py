from django.conf.urls import patterns, include, url
from django.contrib import admin
from table_query_app.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'katalogen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^update/$', import_db),

    url(r'^$', 'login_app.views.index', name='login_home'),
)
