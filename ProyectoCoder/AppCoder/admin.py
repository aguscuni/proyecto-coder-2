from django.contrib import admin

from AppCoder.models import Estudiante, Curso, Profesor, Entregable

# Register your models here.

admin.site.register(Curso)

admin.site.register(Entregable)

admin.site.register(Estudiante)

admin.site.register(Profesor)
