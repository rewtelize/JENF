# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, FormView, View, DetailView

from forms import UserCreateForm
from models import User


def management(request):
	return render(request, 'management.html')

def show_users(request):
	users = User.objects.order_by('country').order_by('firstname').order_by('lastname')
	return render(request, 'users.html', {'users':users})

def delete_user(request, pk):
    return HttpResponse("Delete user")

class UserCreateView(SuccessMessageMixin, CreateView, FormView):
	template_name = "userCreate.html"
	success_url = reverse_lazy("management")
	success_message = "Se ha creado con éxito el usuario"
	form_class = UserCreateForm

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()
		return super(UserCreateView, self).form_valid(form)


