# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView

from AvadaKedavra.management.models import Project

# Create your views here.
def home(request):
	projects = Project.objects.order_by('date')
	return render(request, 'home.html', {'projects':projects})

def exchange(request, pk):
 	project = Project.objects.filter(id=pk).first()
	return render(request, 'exchange.html', {'project': project})
