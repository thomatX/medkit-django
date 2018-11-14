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

class Medicamento(models.Model):
    id = models.CharField(max_length = 10, primary_key=True)
    nombre = models.CharField(max_length = 40)
    contenido = models.CharField(max_length = 10)
    necesita_receta = models.BooleanField(default=False)

class MedicamentoUsuario(models.Model):
    key_id = models.IntegerField(primary_key = True)
    rut = models.CharField(max_length = 20)
    med_id = models.CharField(max_length = 20)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()