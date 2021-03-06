"""AvadaKedavra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from management import views as management_views
from django.conf import settings
from django.conf.urls.static import static
from home import views
from management import views

urlpatterns = [
	url(r'^login/$', management_views.custom_login, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/management'}, name='logout'),
	url(r'^', include('AvadaKedavra.home.urls')),
	url(r'^management/', include('AvadaKedavra.management.urls')),
	url(r'^admin/', include(admin.site.urls))
]
