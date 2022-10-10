from django.shortcuts import render
from AppCoder.models import Estudiante
from django.http import HttpResponse

def ayuda(request):
    return render(request, "AppCoder/ayuda.html")

def inicio(request):
    return render(request, "AppCoder/inicio.html")


def cursos(request):
    return render(request, "AppCoder/cursos.html")
    

def profesores(request):
    return render(request, "AppCoder/profesores.html")


def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")


def entregables(request):
    return render(request, "AppCoder/entregables.html")
