"""BloodBlank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView, ListView

from app import views
from app.models import DonorRegDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.showIndex, name='index'),
    path('home/', views.home, name='home'),
    path('adm/', views.adm, name='adm'),
    path('login/', views.login, name='login'),
    path('donor/', views.donor, name='donor'),
    path('donorhome/', views.donorhome, name='donorhome'),
    path('donorreg/', views.donorreg, name= 'donorreg')
]
