from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    camada = models.IntegerField()

    def __str__(self) -> str:
        return f"({self.camada}) {self.nombre}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()


    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"


