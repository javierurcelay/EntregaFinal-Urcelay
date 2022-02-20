from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('inicio', views.inicio),
    path('carrera/', views.carrera),
    path('curso/', views.curso),
    path('estudiante/', views.estudiante),
    path('matricula/', views.matricula),
    path('contacto/', views.contacto),
]
