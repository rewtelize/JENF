from django.conf.urls import url

from . import views

from django.conf import settings

urlpatterns = [
    url(r'^home', views.home, name='home'),
    url(r'^$', views.home, name='home'),
]
