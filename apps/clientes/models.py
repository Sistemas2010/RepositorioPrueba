from django.db import models


class Cliente(models.Model):
    dni = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=600)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField(verbose_name='Telefono')

    def __str__(self):
        return self.nombre


