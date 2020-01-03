from django.db import models
from django.utils import timezone

# Create your models here.


class Ubicacion(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    creado = models.DateField(auto_now_add=True)
    enUso = models.BooleanField()

    def __str__(self):
        return self.nombre


class Estante(models.Model):
    refUbicacion = models.ForeignKey('Ubicacion', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    creado = models.DateField(auto_now_add=True)
    enUso = models.BooleanField()

    def __str__(self):
        return self.nombre


class Referencia(models.Model):
    nombre = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    codigoBarras = models.CharField(max_length=20)
    unidad = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre


class Alimento(models.Model):
    refEstante = models.ForeignKey('Estante', on_delete=models.CASCADE)
    refReferencia = models.ForeignKey('Referencia', on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=5, decimal_places=2)
    caducidad = models.DateField()

    def __str__(self):
        return self.cantidad
