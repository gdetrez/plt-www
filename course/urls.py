from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to
from views import Exercise1

urlpatterns = patterns(
    '',

    url(r'^$',
        redirect_to, {'url': '/course/week1/'},
        name='home'),
    url(r'^week1/$',
        redirect_to, {'url': '/course/week1/lecture1/'},
        name='week1'),
    url(r'^week1/lecture1/$',
        direct_to_template, {'template': 'week1/lecture1.html'},
        name='week1/lecture1'),
    url(r'^week1/lecture2/$',
        direct_to_template, {'template': 'week1/lecture2.html'},
        name='week1/lecture2'),
    url(r'^week1/exercises/$',
        redirect_to, {'url': '/course/week1/exercises/1/'},
        name='week1/exercises'),
    url(r'^week1/exercises/1/$', Exercise1.as_view(),
        name='week1/exercises/1'),
    url(r'^week1/exercises/2/$', Exercise1.as_view(),
        name='week1/exercises/2'),
    url(r'^week1/lab/$',
        direct_to_template, {'template': 'week1/lab.html'},
        name='week1/lab'),
    url(r'^week1/lab/test-suite/$',
        direct_to_template, {'template': 'week1/lab-test-suite.html'},
        name='week1/lab/test-suite'),
    url(r'^week1/lab/submit/$',
        direct_to_template, {'template': 'week1/lab-submit.html'},
        name='week1/lab/submit'),
)
