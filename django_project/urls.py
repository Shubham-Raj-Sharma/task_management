"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin

# Simple home view that redirects to dashboard if logged in, otherwise to login
class HomeRedirectView(LoginRequiredMixin, RedirectView):
    url = '/tasks/'
    permanent = False

urlpatterns = [
    path('', HomeRedirectView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
]
