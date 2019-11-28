from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('countries:home'))
