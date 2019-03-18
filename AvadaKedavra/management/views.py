# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import redirect, render, render_to_response
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, FormView
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from braces.views import LoginRequiredMixin
from django.contrib.auth.models import User as UserAdmin
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from forms import UserCreateForm, OrganizationCreateForm, UserAdminUpdateForm
from models import Organization, Project, User

import datetime

# Login custom que comprueba si el user esta loggeado en el sistema o no.
def custom_login(request, **kwargs):
	# if request.user.is_authenticated():
	# 	return HttpResponseRedirect(reverse_lazy('management'))
	# else:
	# 	return login(request, **kwargs)
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse_lazy('management'))
	else:
		if request.method == "POST":
			form = AuthenticationForm(request, data=request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				user = authenticate(username=username, password=password)
				if user is not None and user.is_active:
					messages.success(request, "Success in logging.")
					login(request, user)
					return HttpResponseRedirect(reverse_lazy('management'))
			else:
				messages.error(request, "Error! username or password are wrong.")
				return render(request, "registration/login.html", {'form': form})
		else:
			return login(request, **kwargs)

def create_project(request):
	if request.method == "POST":
		form = UserCreateForm(request.POST, request.FILES)
		
		title = request.POST.get("title")
		description = request.POST.get("description")
		country = request.POST.get("country")
		includedCosts = request.POST.get("includedCosts")
		file = request.FILES['file']

		fs = FileSystemStorage()
		filename = fs.save("Image-" + title + ".png", file)
		uploaded_file_url = fs.url(filename)

		p = Project(name=title, description=description, includedCosts=includedCosts, date=datetime.datetime.now())
		p.save()
		return redirect('projects')

	else:
		form = UserCreateForm()

	return render(request, 'exchange_admin.html', {'form':form,})

def delete_project(request, pk):
	Project.objects.filter(id=pk).delete()
	return redirect('projects')

def delete_organization(request, pk):
	Organization.objects.filter(id=pk).delete()
	return redirect('organizations')


class ManagementView(LoginRequiredMixin, TemplateView):
	template_name = "management.html"


# Para que el administrador pueda modificar su usuario.
class UserAdminUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = UserAdmin
	template_name = "userAdminUpdate.html"
	form_class = UserAdminUpdateForm
	success_url = reverse_lazy('management')
	success_message = "Success updating the admin user"

	def form_valid(self, form):
		# Si el user solo quiere cambiar datos que no sea la contraseña, puede dejar esta en blanco, asi conservará
		# su antigüa contraseña.
		if form.data['password'] == '' and form.data['passwordRepeat'] == '':
			self.object = form.save(commit=False)
			self.object.save()
			return super(UserAdminUpdateView, self).form_valid(form)
		elif form.data['password'] != form.data['passwordRepeat']:
			messages.error(self.request, "Passwords are not equal")
			return render(self.request, "userAdminUpdate.html", {'pk': int(self.kwargs['pk']), 'form': form})
		else:
			self.object = form.save(commit=False)
			self.object.set_password(form.data['password'])
			self.object.save()
			return super(UserAdminUpdateView, self).form_valid(form)

# Users
class ListUserView(LoginRequiredMixin, ListView):
	template_name = "users.html"
	model = User

	def get_queryset(self):
		qs = super(ListUserView, self).get_queryset().order_by('country', 'firstname', 'lastname')
		return qs


class UserCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView, FormView):
	template_name = "userCreate.html"
	success_url = reverse_lazy("users")
	success_message = "Success creating the user"
	form_class = UserCreateForm

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()
		return super(UserCreateView, self).form_valid(form)


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	template_name = "userCreate.html"
	model = User
	success_url = reverse_lazy("users")
	success_message = "Success updating the user"
	form_class = UserCreateForm

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()
		return super(UserUpdateView, self).form_valid(form)


class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
	template_name = "delete.html"
	model = User
	success_url = reverse_lazy("users")

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()
		success_url = self.get_success_url()
		self.object.delete()
		messages.success(self.request, "Success deleting the user")
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


class CreateOrganizationView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = "organizationCreate.html"
	model = Organization
	form_class = OrganizationCreateForm
	success_url = reverse_lazy('organizations')
	success_message = "Success creating the organization"

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()
		return super(CreateOrganizationView, self).form_valid(form)


class UpdateOrganizationView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	template_name = "organizationCreate.html"
	model = Organization
	success_url = reverse_lazy('organizations')
	success_message = "Success updating the organization"
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
		messages.success(self.request, "Success deleting the organization")
		return HttpResponseRedirect(success_url)