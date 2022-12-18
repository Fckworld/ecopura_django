from django.views.generic import TemplateView, CreateView
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from usuarios.forms import *
from usuarios.models import Usuario
from ecopuraApp.models import Mensaje


class Registrar(CreateView,SuccessMessageMixin):
    template_name = 'registro.html'
    success_url = reverse_lazy('usuarios:registroexitoso_url')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         nuevo_usuario = Usuario(
    #             correo = form.cleaned_data.get('correo'),
    #        )
    #         correo = form.cleaned_data.get('correo')
    #         print(correo)
    #         #SI ENCUENTRO UN USUARIO CON EL MISMO CORREO CON EL MENSAJE
            
    #     return  HttpResponse('hola')


class Link(TemplateView):
    template_name = 'link.html'

class RegistroExitoso(TemplateView):
    template_name = 'registro-exitoso.html'

class CerrarSesion(LogoutView):
    next_page='ecopuraApp:inicio_url'
    
class IniciarSession(CreateView):
    template_name = 'login2.html'
    success_url = reverse_lazy('usuarios:registroexitoso_url')
    form_class = InicioSessionForm

class IniciarSesion(LoginView):
    template_name = 'login.html'
    form_class = InicioSesionForm
    next_page='ecopuraApp:inicio_url'

class CarroInvitado(CreateView):
    template_name='carro-invitado.html'

    #success_url = reverse_lazy('usuarios:registroexitoso_url') CAMBIAR POR CONFIRMACION DE CLIENTE. 



