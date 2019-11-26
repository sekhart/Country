# Generated by Django 2.2.7 on 2019-11-26 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=250, verbose_name='Country Name')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.TextField()),
                ('state_capital', models.TextField()),
                ('total_districts', models.IntegerField()),
                ('country_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='countries.Country')),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
        ),
    ]
