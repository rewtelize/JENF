from django.conf.urls import url

from . import views
from django.conf import settings
from views import UserCreateView

urlpatterns = [
    url(r'^deleteUser/(?P<pk>[0-9a-f-]+)/$', views.delete_user, name='delete_user'),
    url(r'^deleteOrganization/(?P<pk>[0-9a-f-]+)/$', views.delete_organization, name='delete_organization'),
    url(r'^deleteProject/(?P<pk>[0-9a-f-]+)/$', views.delete_project, name='delete_project'),
    url(r'^management/', views.management, name='management'),
    url(r'^organizations', views.show_organizations, name='organizations'),
    url(r'^projects', views.ListProjectView.as_view(), name='projects'),
    # Users
    url(r'^users', views.ListUserView.as_view(), name='users'),
    url(r'^crearUsuario', UserCreateView.as_view(), name="create-user"),
    url(r'^updateUser/(?P<pk>[0-9a-f-])/$', views.UserUpdateView.as_view(), name="update-user"),
    url(r'^$', views.management, name='management'),
]
