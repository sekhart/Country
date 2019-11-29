from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Country(models.Model):
    country_name = models.CharField('Country Name', max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.country_name


class States(models.Model):
    country_name = models.ForeignKey(Country, on_delete=models.PROTECT)
    state_name = models.CharField('State Name', max_length=250)
    state_capital = models.CharField('Capital', max_length=250)
    total_districts = models.IntegerField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'states'

    def __str__(self):
        return self.state_name[:250]


