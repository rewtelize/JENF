from django.conf.urls import url

from . import views

from django.conf import settings

urlpatterns = [
    url(r'^home', views.home, name='home'),
    url(r'^exchange', views.exchange, name='exchange'),
    url(r'^$', views.home, name='home'),
]
