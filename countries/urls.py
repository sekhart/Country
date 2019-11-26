"""Defines URL patterns for countries."""
from django.conf.urls import url
from . import views

app_name = 'countries'
urlpatterns = [
    # Home Page
    url('^$', views.home, name='home'),
    url('^index/$', views.index, name='index'),
    url('^countries/$', views.countries, name='countries'),
    url('stateslist/(?P<country_id>\d+)/$', views.stateslist, name='stateslist')
]