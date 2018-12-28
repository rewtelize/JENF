from django.conf.urls import url

from . import views
from django.conf import settings
from views import UserCreateView

urlpatterns = [
    url(r'^management/', views.management, name='management'),
    url(r'^$', views.management, name='management'),
    url(r'^crearUsuario', UserCreateView.as_view(), name="create-user"),
]
