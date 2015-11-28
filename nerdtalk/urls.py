from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse
from menu import Menu, MenuItem

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'nerdtalk.views.home', name='home'),
    url(r'^auth/', include('auth.urls')),
)

