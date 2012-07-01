from django.conf.urls.defaults import patterns, include, url
from ghatiparty import views

# For serving static files on development environment
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, {'mood': 'ghatipan-heaven'}),
    url(r'^music/(?P<mood>[A-Za-z\-]+)/$', views.index),
    # url(r'^ghati/', include('ghati.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# For serving static files on development environment
urlpatterns += staticfiles_urlpatterns()
