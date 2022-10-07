from django.shortcuts import render
from AppCoder.models import Estudiante

def mostrar_inicio(request):
    estudiante = Estudiante(nombre="Exequiel", apellido="Velazquez", email="eze@gmail.com")
    estudiante.save()
    contexto = {"estudiante_1": estudiante}
    return render(request, "AppCoder/inicio.html", contexto)
