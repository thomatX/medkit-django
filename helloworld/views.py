# helloworld/views.py
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class ContactPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'contacto.html', context=None)

class AccountPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'cuenta.html', context=None)

class LoginPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'login.html', context=None)

class MedsPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'medicamentos.html', context=None)

class RequestPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'solicitud.html', context=None)