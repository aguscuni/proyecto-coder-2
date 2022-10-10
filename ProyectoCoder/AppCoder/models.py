from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()


    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"