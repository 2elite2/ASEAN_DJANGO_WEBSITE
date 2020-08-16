

from django.contrib import admin
from django.urls import path
from NBO import views

urlpatterns = [
    path("", views.index, name='NBO'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),



]
