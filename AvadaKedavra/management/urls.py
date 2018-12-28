from django.conf.urls import url

from . import views
from django.conf import settings
from views import UserCreateView

urlpatterns = [
    url(r'^management/', views.management, name='management'),
    url(r'^crearUsuario', UserCreateView.as_view(), name="create-user"),
    url(r'^deleteUser/(?P<pk>[0-9a-f-]+)/$', views.delete_user, name='delete_user'),
    url(r'^users', views.show_users, name='users'),
    url(r'^$', views.management, name='management'),
]
