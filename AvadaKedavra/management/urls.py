from django.conf.urls import url

from . import views

from django.conf import settings

urlpatterns = [
    url(r'^management/', views.management, name='management'),
    url(r'^$', views.management, name='management'),
]
