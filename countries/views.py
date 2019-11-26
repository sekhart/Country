from django.shortcuts import render

from .models import Country, States


def home(request):
    """The home page for Countries"""
    print('home page')
    return render(request, 'countries/home.html')


def index(request):
    print('index page')
    return render(request, 'countries/index.html')


def countries(request):
    """The countries page for Countries"""
    cntrs = Country.objects.order_by('country_name')
    context = {'countries': cntrs}
    return render(request, 'countries/countries.html', context)


def stateslist(request, country_id):
    """The states page for Countries"""
    s = Country.objects.get(id=country_id)
    states_info = s.states_set.order_by('-date_added')
    context = {'state': s, 'stateslist': states_info}
    return render(request, 'countries/stateslist.html', context)
