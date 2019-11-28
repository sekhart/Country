from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Country, States

from .forms import CountryForm, StateForm


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


def new_country(request):
    """Add new Country"""
    if request.method != 'POST':
        form = CountryForm()
    else:
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('countries:countries'))
    context = {'form': form}
    return render(request, 'countries/new_country.html', context)


def new_state(request, country_id):
    """Add new State for a particular country"""
    country = Country.objects.get(id=country_id)
    if request.method != 'POST':
        form = StateForm()
    else:
        form = StateForm(request.POST)
        if form.is_valid():
            newstate = form.save(commit=False)
            newstate.country = country
            newstate.country_name_id = country_id
            newstate.save()
            return HttpResponseRedirect(reverse('countries:stateslist', args=[country_id]))
    context = {'country': country, 'form': form}
    return render(request, 'countries/new_state.html', context)


def edit_state(request, state_id):
    """Edit State for a particular country"""
    state = States.objects.get(id=state_id)
    country = state.country_name

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = StateForm(instance=state)
    else:
        # POST data submitted; process data.
        form = StateForm(instance=state, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('countries:stateslist', args=[country.id]))
    context = {'state': state, 'country': country, 'form': form}
    return render(request, 'countries/edit_state.html', context)


