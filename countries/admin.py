from django.contrib import admin

# Register your models here.
from .models import Country, States

admin.site.register(Country)
admin.site.register(States)