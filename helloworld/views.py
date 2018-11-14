# helloworld/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Usuario, Medicamento, MedicamentoUsuario
from django.core import serializers
from django.http import JsonResponse
import json
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

#importar user
from django.contrib.auth.models import User
#sistema de autenticación 
from django.contrib.auth import authenticate,logout, login as auth_login

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def homePage(request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def contactPage(request):
    return render(request, 'contacto.html')

@login_required(login_url='/login/')
def accountPage(request):
    return render(request, 'cuenta.html')

@login_required(login_url='/login/')


def medsPage(request):
    rut = request.user.username
    medicamentos_user_object = MedicamentoUsuario.objects.all().filter(rut=rut)
    meds_user = []
    for x in medicamentos_user_object:
        med = Medicamento.objects.get(id=x.med_id)
        current = {"id":x.med_id,"nombre":med.nombre,"fecha_inicio":x.fecha_inicio,"fecha_termino":x.fecha_termino,"contenido":med.contenido}
        print(current)
        meds_user.append(current)
    return render(request, 'medicamentos.html', 
        {
            "medicamentos_usuario":meds_user,
            "rut":rut
        })    

@login_required(login_url='/login/')
def requestPage(request):
    return render(request, 'solicitud.html')
    
    
def loginPage(request):
    return render(request, 'login.html')
    
def registerPage(request):
    return render(request, 'register.html')

def createUser(request):
    try:
        email = request.POST.get('email')
        rut = request.POST.get('rut')
        name = request.POST.get('name')
        born = request.POST.get('born')
        number = request.POST.get('number')
        region = request.POST.get('region')
        comuna = request.POST.get('comuna')
        password = request.POST.get('password')
        direccion = request.POST.get('direccion')
        user = Usuario(email=email, rut=rut, nombre=name, fecha_nacimiento=born, numero_telefono=number, region=region, comuna=comuna, direccion=direccion, password=password)
        user.save()
        userAuth = User.objects.create_user(rut, email=email, password=password)
        userAuth.save()
        return HttpResponse('<script>alert("Usuario registrado correctamente!"); window.location.href="/login/";</script>')

    except Exception as ex:
        return HttpResponse('<script>alert("Se ha ingresado un valor incorrecto... Intenta nuevamente."); window.location.href="/register/";</script>')


@login_required(login_url='/login/')
def cerrar_session(request):
    logout(request)
    return HttpResponse('<script>alert("Cierre de sesión correcto."); window.location.href="/login/";</script>')


def login_iniciar(request):
    usuario = request.POST.get('rut','')
    contrasenia = request.POST.get('contrasenia','')
    user = authenticate(request,username=usuario, password=contrasenia)

    if user is not None:
        auth_login(request, user)
        return HttpResponse('<script>alert("Inicio de sesión correcto."); window.location.href="/";</script>')
    else:
        return HttpResponse('<script>alert("Ocurrió un error, intenta nuevamente..."); window.location.href="/login/";</script>')
