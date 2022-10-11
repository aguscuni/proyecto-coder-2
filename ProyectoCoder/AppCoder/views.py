from django.shortcuts import render
from AppCoder.models import Estudiante, Curso
from django.http import HttpResponse

from AppCoder.forms import CursoFormulario


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


def procesar_formulario(request):

    if request.method != "POST":
        return render(request, "AppCoder/formulario.html")

    curso = Curso(nombre=request.POST["curso"], camada=request.POST["camada"])
    curso.save()

    return render(request, "AppCoder/inicio.html")


def procesar_formulario_2(request):
    if request.method != "POST":
        mi_formulario = CursoFormulario()
    else:
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "AppCoder/inicio.html")

    contexto = {"formulario": mi_formulario}

    return render(request, "AppCoder/formulario_2.html", contexto)


def busqueda(request):
    return render(request, "AppCoder/busqueda.html")


def buscar(request):
    respuesta = f"Estoy buscando la camada número: {request.GET['camada']}"

    return HttpResponse(respuesta)


def busqueda_2(request):
    return render(request, "AppCoder/busqueda_2.html")


def buscar_2(request):

    if not request.GET["camada"]:
        return HttpResponse("No enviaste datos")
    else:
        camada_a_buscar = request.GET["camada"]
        cursos = Curso.objects.filter(camada=camada_a_buscar)

        contexto = {"camada": camada_a_buscar, "cursos_encontrados": cursos}

        return render(request, "AppCoder/resultado_busqueda.html", contexto)
