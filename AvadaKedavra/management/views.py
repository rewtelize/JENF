# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, FormView, View, DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from braces.views import LoginRequiredMixin, GroupRequiredMixin

from forms import UserCreateForm, OrganizationCreateForm
from models import Organization, Project, User

# Login custom que comprueba si el user esta loggeado en el sistema o no.
def custom_login(request, **kwargs):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse_lazy('management'))
	else:
		return login(request, **kwargs)


def delete_organization(request, pk):
	Organization.objects.filter(id=pk).delete()
	return redirect('organizations')


class ManagementView(LoginRequiredMixin, TemplateView):
	template_name = "management.html"


# Users
class ListUserView(LoginRequiredMixin, ListView):
	template_name = "users.html"
	model = User
	# group_required = ['Administrador'] Tenemos que implementar grupos ya que si no cualquiera podría acceder a la url.

	def get_queryset(self):
		qs = super(ListUserView, self).get_queryset().order_by('country', 'firstname', 'lastname')
		return qs


class UserCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView, FormView):
	template_name = "userCreate.html"
	success_url = reverse_lazy("users")
	success_message = "Se ha creado con éxito el usuario"
	form_class = UserCreateForm

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()
		return super(UserCreateView, self).form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
	template_name = "userCreate.html"
	model = User
	success_url = reverse_lazy("users")
	form_class = UserCreateForm

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()
		return super(UserUpdateView, self).form_valid(form)


class UserDeleteView(LoginRequiredMixin, DeleteView):
	template_name = "delete.html"
	model = User
	success_url = reverse_lazy("users")

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()
		success_url = self.get_success_url()
		self.object.delete()
		return HttpResponseRedirect(success_url)


# Projects
class ListProjectView(LoginRequiredMixin, ListView):
	template_name = "projects.html"
	model = Project
	# group_required = ['Administrador']

	def get_queryset(self):
		qs = super(ListProjectView, self).get_queryset().order_by('country')
		return qs


# Organizations
class ListOrganizationView(LoginRequiredMixin, ListView):
	template_name = "organizations.html"
	model = Organization
	context_object_name = "organizations"

	def get_queryset(self):
		qs = super(ListOrganizationView, self).get_queryset().order_by('country', 'name')
		return qs


class CreateOrganizationView(LoginRequiredMixin, CreateView):
	template_name = "organizationCreate.html"
	model = Organization
	form_class = OrganizationCreateForm
	success_url = reverse_lazy('organizations')

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()
		return super(CreateOrganizationView, self).form_valid(form)


class UpdateOrganizationView(LoginRequiredMixin, UpdateView):
	template_name = "organizationCreate.html"
	model = Organization
	success_url = reverse_lazy('organizations')
	form_class = OrganizationCreateForm

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()
		return super(UpdateOrganizationView, self).form_valid(form)


class DeleteOrganizationView(LoginRequiredMixin, DeleteView):
	template_name = "delete.html"
	model = Organization
	success_url = reverse_lazy('organizations')

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()
		success_url = self.get_success_url()
		self.object.delete()
		return HttpResponseRedirect(success_url)