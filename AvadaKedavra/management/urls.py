from django.conf.urls import url

from . import views
from django.conf import settings
from views import UserCreateView
from django.contrib.auth.views import password_change

urlpatterns = [
    # url(r'^deleteProject/(?P<pk>[0-9a-f-]+)/$', views.delete_project, name='delete_project'),
    url(r'^management/', views.ManagementView.as_view(), name='management'),
    url(r'^projects', views.ListProjectView.as_view(), name='projects'),
    # Users
    url(r'^users', views.ListUserView.as_view(), name='users'),
    url(r'^crearUsuario', UserCreateView.as_view(), name="create-user"),
    url(r'^updateUser/(?P<pk>[0-9a-f-])/$', views.UserUpdateView.as_view(), name="update-user"),
    url(r'^deleteUser/(?P<pk>[0-9a-f-]+)/$', views.UserDeleteView.as_view(), name="delete-user"),
    url(r'^$', views.ManagementView.as_view(), name='management'),
    # Organizations
    url(r'^organizations', views.ListOrganizationView.as_view(), name='organizations'),
    url(r'^createOrganization/$', views.CreateOrganizationView.as_view(), name='create-organization'),
    url(r'^deleteOrganization/(?P<pk>[0-9a-f-]+)/$', views.DeleteOrganizationView.as_view(),
        name='delete-organization'),
    url(r'^updateOrganization/(?P<pk>[0-9a-f-]+)/$', views.UpdateOrganizationView.as_view(),
        name='update-organization'),
    # Admin User
    url(r'^updateUserAdmin/(?P<pk>[0-9a-f-]+)/$', views.UserAdminUpdateView.as_view(),
        name='update-userAdmin'),
]
