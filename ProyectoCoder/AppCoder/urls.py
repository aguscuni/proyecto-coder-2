"""ProyectoCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from AppCoder import views

urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("cursos", views.cursos, name="Cursos"),
    path("profesores", views.profesores, name="Profesores"),
    path("estudiantes", views.estudiantes, name="Estudiantes"),
    path("entregables", views.entregables, name="Entregables"),
    path("formulario", views.procesar_formulario, name="formulario"),
    path("formulario-2", views.procesar_formulario_2, name="formulario_2"),
    path("busqueda", views.busqueda, name="busqueda"),
    path("busqueda-2", views.busqueda_2, name="busqueda_2"),
    path("buscar", views.buscar, name="buscar"),
    path("buscar-2", views.buscar_2, name="buscar_2"),
]
