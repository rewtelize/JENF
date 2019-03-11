from django.conf.urls import url

from . import views

from django.conf import settings

urlpatterns = [
	url(r'exchange/(?P<pk>[0-9A-Za-z_\-]+)/$', views.exchange, name="exchange"),
    url(r'^home', views.home, name='home'),
    url(r'^$', views.home, name='home'),
]
