# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, FormView, View, DetailView

from forms import UserCreateForm
from models import Organization, Project, User


def management(request):
	return render(request, 'management.html')

def show_organizations(request):
	organizations = Organization.objects.order_by('country').order_by('name')
	return render(request, 'organizations.html', {'organizations':organizations})

def show_projects(request):
	projects = Project.objects.order_by('country')
	return render(request, 'projects.html', {'projects':projects})


def delete_organization(request, pk):
	Organization.objects.filter(id=pk).delete()
	return redirect('organizations')

def delete_project(request, pk):
	Project.objects.filter(id=pk).delete()
	return redirect('projects')

def delete_user(request, pk):
	User.objects.filter(id=pk).delete()
	return redirect('users')


class UserCreateView(SuccessMessageMixin, CreateView, FormView):
	template_name = "userCreate.html"
	success_url = reverse_lazy("users")
	success_message = "Se ha creado con éxito el usuario"
	form_class = UserCreateForm

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()
		return super(UserCreateView, self).form_valid(form)


class ListUserView(ListView):
	template_name = "users.html"
	model = User
	# group_required = ['Administrador'] Tenemos que implementar grupos ya que si no cualquiera podría acceder a la url.

	def get_queryset(self):
		qs = super(ListUserView, self).get_queryset().order_by('country', 'firstname', 'lastname')
		return qs

