from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cvimapp.views.index'),
    url(r'^cvs/$', 'cvimapp.views.list_cvs'),
    url(r'^cvs/save/$', 'cvimapp.views.save_cv'),
    url(r'^cvs/(?P<cv_id>\d+)', 'cvimapp.views.detail_cv'),
    url(r'^experience/$', 'cvimapp.views.list_experiences'),
    url(r'^experience/save/$', 'cvimapp.views.save_experience'),
    url(r'^friends/$', 'cvimapp.views.list_friends'),
    url(r'^friend/(?P<friend_id>\d+)', 'cvimapp.views.detail_friend'),
    url(r'^login/$', 'cvimapp.views.login'),
    # url(r'^cvim/', include('cvim.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
