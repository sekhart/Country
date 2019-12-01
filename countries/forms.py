from django import forms

from .models import Country, States


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['country_name']
        labels = {'country_name': ''}


class StateForm(forms.ModelForm):
    class Meta:
        model = States
        fields = ['state_name', 'state_capital', 'total_districts']
        labels = {'state_name': 'State ', 'state_capital': 'Capital ', 'total_districts': 'No. Districts '}
        widgets = {'state_name': forms.TextInput(attrs={'size': 20, 'title': 'State'}),
                   'state_capital': forms.TextInput(attrs={'size': 20, 'title': 'Capital'}),
                   'total_districts': forms.NumberInput()}
