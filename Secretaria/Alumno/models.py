from time import strftime
from typing import TextIO
from xmlrpc.client import _strftime
from django.db import models

# Create your models here.

class Carrera(models.Model):
    nombre = models.CharField(max_length=40)
    duracion = models.PositiveSmallIntegerField(default=5)
    
    turnos = [
        ('M', 'Mañana'),
        ('T', 'Tarde'),
        ('N', 'Noche')
    ]
    
    turno = models.CharField(max_length=1, choices=turnos, default='M')
    
    
    def __str__(self):
        texto = '{0} (Duración: {1} año(s))'
        return texto.format(self.nombre, self.duracion)
        
class Estudiante(models.Model):
    apellido = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    dni = models.CharField(max_length=8)
    nacimiento = models.DateField()
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    
    def nombreCompleto(self):
        texto = '{0} {1}'
        return texto.format(self.apellido, self.nombre)
    
    def __str__(self):
        texto = '{0} / Carrera: {1} / {2}'
        if self.estado:
            habilitacion = 'Habilitado'
        else:
            habilitacion = 'Inhabilitado'
        return texto.format(self.nombreCompleto(), self.carrera, habilitacion)        
    
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    duracion = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=30)
    
    def __str__(self):
        texto = '{0}, {1} / Doncente: {2}'
        return texto.format(self.nombre, self.duracion, self.docente)
    
class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        texto = 'Matriculado {0} {1}'
        return texto.format(self.estudiante, self.curso)
    