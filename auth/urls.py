from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse
from menu import MenuItem, Menu

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'auth.views.home', name='home'),
    url(r'^login$', 'auth.views.login', name='login'),
)

