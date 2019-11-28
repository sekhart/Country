"""Defines URL patterns for countries."""
from django.conf.urls import url
from . import views

app_name = 'countries'
urlpatterns = [
    # Home Page
    url('^$', views.home, name='home'),
    url('^index/$', views.index, name='index'),
    url('^countries/$', views.countries, name='countries'),
    url('stateslist/(?P<country_id>\d+)/$', views.stateslist, name='stateslist'),
    url('new_country/$', views.new_country, name='new_country'),
    url('^new_state/(?P<country_id>\d+)/$', views.new_state, name='new_state'),
]