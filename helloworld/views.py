# helloworld/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Usuario, Medicamento, MedicamentoUsuario, TarjetaCredito
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
    # User attributes
    rut = request.user.username
    medicamentos_user_object = MedicamentoUsuario.objects.all().filter(rut=rut)
    cantidad = len(medicamentos_user_object)
    return render(request, 'index.html', 
        {
            'medicamentos_activos':cantidad
        })

@login_required(login_url='/login/')
def contactPage(request):
    return render(request, 'contacto.html')

@login_required(login_url='/login/')
def accountPage(request):
    rut = request.user.username
    user = Usuario.objects.all().filter(pk=rut)
    card = TarjetaCredito.objects.all().filter(pk=rut)
    return render(request, 'cuenta.html',  
        {
            'active_user':user,
            'credit_card':card
        })


@login_required(login_url='/login/')
def medsPage(request):
    rut = request.user.username
    medicamentos_user_object = MedicamentoUsuario.objects.all().filter(rut=rut)
    meds_user = []
    for x in medicamentos_user_object:
        med = Medicamento.objects.get(id=x.med_id)
        current = {"pk":x.key_id,"id":x.med_id,"nombre":med.nombre,"cantidad":x.cantidad,"fecha_inicio":x.fecha_inicio,"fecha_termino":x.fecha_termino,"contenido":med.contenido,"metodo_pago":x.pay_method}
        print(current)
        meds_user.append(current)
    return render(request, 'medicamentos.html', 
        {
            "medicamentos_usuario":meds_user,
            "rut":rut
        })

def delete_meds(request, pk, template_name='meds_confirm_delete.html'):
    med = get_object_or_404(MedicamentoUsuario, pk=pk)    
    if request.method=='POST':
        med.delete()
        return redirect('/meds/')
    return render(request, template_name, {'object':med}) 

def delete_card(request, pk, template_name='card_confirm_delete.html'):
    card = get_object_or_404(TarjetaCredito, pk=pk)    
    if request.method=='POST':
        card.delete()
        return redirect('/account/')
    return render(request, template_name, {'object':card})    

@login_required(login_url='/login/')
def requestPage(request):
    meds = Medicamento.objects.all()
    rut = request.user.username
    card = TarjetaCredito.objects.all().filter(pk=rut)
    return render(request, 'solicitud.html', {"medicamentos":meds,"credit_card":card})
    
    
def loginPage(request):
    return render(request, 'login.html')
    
def registerPage(request):
    return render(request, 'register.html')

@login_required(login_url='/login/')
def card_edit(request):
    try:
        rut = request.user.username
        card = TarjetaCredito.objects.get(pk = rut)
        card.nombre = request.POST.get('cardname')
        card.numero_tarjeta = request.POST.get('cardnumber')
        card.banco = request.POST.get('cardbank')
        card.mes = request.POST.get('cardmonth')
        card.year = request.POST.get('cardyear')
        card.clave_secreta = request.POST.get('cardpass')
        card.save()
        return HttpResponse('<script>alert("Los datos se han actualizado correctamente!"); window.location.href="/account/";</script>')
    except Exception as ex:
        return HttpResponse('<script>alert("Ha ocurrido un error, intenta nuevamente..."); window.location.href="/account/";</script>')


@login_required(login_url='/login/')
def user_med_register(request):
    try:

        user_meds = MedicamentoUsuario.objects.all()
        cantidad = len(user_meds)

        med_id = request.POST.get('medname')
        medicamento = Medicamento.objects.get(id=med_id)

        key_id = cantidad+1
        rut = request.user.username
        fecha_inicio = request.POST.get('start')
        fecha_termino = request.POST.get('end')
        cantidad = request.POST.get('quantity')
        metodo_pago = request.POST.get('payMethod')
        med_usuario = MedicamentoUsuario(key_id=key_id, rut=rut, med_id=med_id, cantidad=cantidad, pay_method=metodo_pago, fecha_inicio=fecha_inicio,fecha_termino=fecha_termino)
        med_usuario.save()
        return HttpResponse('<script>alert("Medicamento registrado correctamente!"); window.location.href="/meds/";</script>')
    except Exception as ex:
        return HttpResponse('<script>alert("Ha ocurrido un error, intenta nuevamente..."); window.location.href="/request/";</script>')


@login_required(login_url='/login/')
def card_register(request):
    try:
        rut = request.user.username
        nombre = request.POST.get('cardname')
        numero_tarjeta = request.POST.get('cardnumber')
        banco = request.POST.get('cardbank')
        clave_secreta = request.POST.get('cardpass')
        mes = request.POST.get('cardmonth')
        year = request.POST.get('cardyear')
        card = TarjetaCredito(rut=rut, nombre=nombre, numero_tarjeta=numero_tarjeta, banco=banco, mes=mes, year=year, clave_secreta=clave_secreta)
        card.save()
        return HttpResponse('<script>alert("Tarjeta registrada correctamente!"); window.location.href="/account/";</script>')
    except Exception as ex:
        return HttpResponse('<script>alert("Ha ocurrido un error, intenta nuevamente..."); window.location.href="/account/";</script>')


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
        userAuth = User.objects.create_user(rut, email=email, password=password)
        userAuth.save()
        user = Usuario(email=email, rut=rut, nombre=name, fecha_nacimiento=born, numero_telefono=number, region=region, comuna=comuna, direccion=direccion, password=password)
        user.save()
        
        return HttpResponse('<script>alert("Usuario registrado correctamente!"); window.location.href="/login/";</script>')

    except Exception as ex:
        return HttpResponse('<script>alert("Se ha ingresado un valor incorrecto... Intenta nuevamente."); window.location.href="/register/";</script>')

@login_required(login_url='/login/')
def editUser(request):
    try:
        rut = request.user.username
        user = Usuario.objects.get(pk = rut)
        user.nombre = request.POST.get('name')
        user.email = request.POST.get('email')
        user.direccion = request.POST.get('adress')
        user.numero_telefono = request.POST.get('phone')
        user.save()
        return HttpResponse('<script>alert("Los datos se han actualizado correctamente!"); window.location.href="/account/";</script>')
    except Exception as ex:
        return HttpResponse('<script>alert("Ha ocurrido un error, intenta nuevamente..."); window.location.href="/account/";</script>')

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
