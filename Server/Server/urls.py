"""Server URL Configuration

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
from REST_API.views import *
urlpatterns = [
    path('readAll', readAll, name = "readAll"),
    path('createCity', createCity, name='createCity'),
    path('createFirm', createFirm, name='createFirm'),
    path('createHuman', createHuman, name='createHuman'),
    path('createReligion', createReligion, name='createReligion'),


    path('deleteCity', deleteCity, name="deleteCity"),
    path('deleteFirm', deleteFirm, name="deleteFirm"),
    path('deleteHuman', deleteHuman, name="deleteHuman"),
    path('deleteReligion', deleteReligion, name="deleteReligion"),


    path('updateCity', updateCity, name="updateCity"),
    path('updateFirm', updateFirm, name="updateFirm"),
    path('updateHuman', updateHuman, name="updateHuman"),
    path('updateReligion', updateReligion, name="updateReligion"),
]
