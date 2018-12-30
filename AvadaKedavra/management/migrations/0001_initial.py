# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-30 17:32
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name of the organization')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Description of the organization.')),
                ('country', django_countries.fields.CountryField(max_length=746, multiple=True, verbose_name='Country')),
                ('president', models.CharField(max_length=50, verbose_name="President's name.")),
                ('president_email', models.EmailField(max_length=254, verbose_name="President's name")),
                ('president_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name="President's phone")),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="Project's name.")),
                ('code', models.CharField(max_length=20, verbose_name='Code of the project.')),
                ('country', django_countries.fields.CountryField(max_length=746, multiple=True, verbose_name='Country')),
                ('city', models.CharField(max_length=40, verbose_name='City')),
                ('date', models.DateField(verbose_name='Date')),
                ('organization', models.ManyToManyField(to='management.Organization', verbose_name='Organizations')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30, verbose_name="User's First Name")),
                ('lastname', models.CharField(max_length=60, verbose_name="User's Last Name")),
                ('country', django_countries.fields.CountryField(max_length=746, multiple=True, verbose_name='Country')),
                ('birthdate', models.DateField(verbose_name='Birthdate')),
                ('residence', models.CharField(max_length=50, verbose_name='City where you live')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name="User's phone number")),
                ('project', models.ManyToManyField(help_text='Specify the project/s that you want to assign to the user (using CTRLyou have a multiple selection', to='management.Project', verbose_name='Projects')),
            ],
        ),
    ]
