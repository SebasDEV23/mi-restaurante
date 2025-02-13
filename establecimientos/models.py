from django.db import models
from django.contrib.auth.models import User

class Establecimiento(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    administrador = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True, blank=True, upload_to='establecimientos/')

    def __str__(self):
        return self.nombre