from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.CharField(max_length = 40)
    rut = models.CharField(max_length = 20, primary_key=True)
    nombre = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 50)
    fecha_nacimiento = models.DateField()
    numero_telefono = models.IntegerField()
    region = models.CharField(max_length = 60)
    comuna = models.CharField(max_length = 60)
    password = models.CharField(max_length = 30)