from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
# Create your views here.


def inicio(request):
    return render(request,'Inicio.html')

def carrera(request):
    carreras = Carrera.objects.all()
    return render(request,'Carrera.html', {'carreras': carreras})


def curso(request):
    cursos = Curso.objects.all()
    return render(request,'Curso.html',{'cursos': cursos})


def estudiante(request):
    estudiantes = Estudiante.objects.all()
    return render(request,'Estudiante.html', {'estudiantes': estudiantes})


def matricula(request):
    matriculas = Matricula.objects.all()
    return render(request,'Matricula.html',{'matriculas': matriculas})

def contacto(request):
    return render(request,'Contacto.html')
