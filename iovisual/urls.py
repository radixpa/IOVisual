from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login$', 'iovisual.utils.views.login', name='login'),
    url(r'^logout$', 'iovisual.utils.views.logout', name='logout'),


    url(r'^', include('iovisual.campana.urls')),

    # Examples:
    # url(r'^$', 'iovisual.views.home', name='home'),
    # url(r'^iovisual/', include('iovisual.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
