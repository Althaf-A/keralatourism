"""keralatourism URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('explore/', views.explore),
    path('palakkad/', views.palakkad),
    path('thrissur/', views.thrissur),
    path('wayanad/', views.wayanad),
    path('kasargod/', views.kasargod),
    path('malappuram/', views.malappuram),
    path('Thiruvananthapuram/', views.Thiruvananthapuram),
    path('kannur/', views.kannur),
    path('calicut/', views.calicut),
    path('Ernakulam/', views.Ernakulam),
    path('kollam/', views.kollam),
    path('idduki/', views.idduki),
    path('pathanamthitta/', views.pathanamthitta),
    path('alapuzha/', views.alapuzha),
    path('kottayam/', views.kottayam),
   path('register/', views.register),
   path('save/', views.save),
    
]
