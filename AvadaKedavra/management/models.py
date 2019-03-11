# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


class Organization(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name="Name of the organization")
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name="Description of the organization.")
    country = CountryField(verbose_name="Country", multiple=True) #La opción multiple permite seleccionar varios países
    president = models.CharField(max_length=50, null=False, verbose_name="President's name.")
    president_email = models.EmailField(null=False, verbose_name="President's email")
    president_phone = PhoneNumberField(verbose_name="President's phone")


    def __unicode__(self):
        return "{}".format(self.name)


class Project(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name="Project's name.")
    code = models.CharField(max_length=20, null=False, verbose_name="Code of the project.")
    country = CountryField(verbose_name="Country", multiple=True)
    # Falta por implementar para city algo parecido al choices de country.
    city = models.CharField(max_length=40, null=False, verbose_name="City")
    date = models.DateField(null=False, verbose_name="Date")
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __unicode__(self):
        return "{}".format(self.name)


class User(models.Model):
    firstname = models.CharField(max_length=30, null=False, verbose_name="User's First Name")
    lastname = models.CharField(max_length=60, null=False, verbose_name="User's Last Name")
    country = CountryField(verbose_name="Country", multiple=True)
    birthdate = models.DateField(null=False, verbose_name="Birthdate")
    residence = models.CharField(max_length=50, null=False, verbose_name="Residence")
    email = models.EmailField(null=False, verbose_name="Email")
    phone = PhoneNumberField(verbose_name="User's phone number")
    project = models.ManyToManyField(Project, verbose_name="Projects",
                                     help_text="Specify the project/s that you want to assign to the user (using CTRL"
                                               "you have a multiple selection")

    def __unicode__(self):
        return '%s, %s' % (self.lastname, self.firstname)
