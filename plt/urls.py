from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'plt.views.home', name='home'),
    url(r'^info/', direct_to_template, {'template': 'info.html'}, name='info'),
    url(r'^contact/', direct_to_template, {'template': 'contact.html'}, name='contact'),
    url(r'^course/', include('course.urls', namespace="course")),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
