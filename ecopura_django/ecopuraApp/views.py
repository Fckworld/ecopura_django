from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render

from ecopuraApp.models import *
from ecopuraApp.forms import *

# Create your views here.

class Inicio(ListView):
    template_name= 'inicio.html'
    model = Producto
    paginate_by = 9
    ordering = ['nombre']

class ProductoDetalle(DetailView):
    model = Producto
    template_name = 'producto_detalle.html'

class Agua(ListView):
    template_name='agua.html'
    model = Producto
    paginate_by = 9
    ordering= ['nombre']
    def get_queryset(self):
        return Producto.objects.filter(tipo_id = 1)

    context_object_name = 'productos'
    
class CrearContacto(CreateView):
    model = Mensaje
    template_name='contacto.html'
    form_class = CrearContactoForm
    success_url= reverse_lazy('ecopuraApp:contacto_url')
    
    #Considerar que cuando llamo a la funcion post, tengo que sobre escribir
    #tanto si esta validando como el save.
    def post(self, request, *args, **kwargs):
        form =  self.form_class(request.POST)
        if form.is_valid():
            nuevo_mensaje = Mensaje(
                p_nombre = form.cleaned_data.get('p_nombre'),
                p_apellido = form.cleaned_data.get('p_apellido'),
                empresa = form.cleaned_data.get('empresa'),
                telefono = form.cleaned_data.get('telefono'),
                rut_empresa = form.cleaned_data.get('rut_empresa'),
                correo = form.cleaned_data.get('correo'),
                detalle_dispensador = form.cleaned_data.get('detalle_dispensador'),
                detalle_texto = form.cleaned_data.get('detalle_texto'),
                creacion = form.cleaned_data.get('creacion'),
            )
            cv = str(nuevo_mensaje.rut_empresa).partition('-')[2]
            nuevo_mensaje.rut_ver_empresa = cv
            print('He guardado el mensaje')
            print(nuevo_mensaje.correo)
            print('AHORA VERIFICO SI EXISTE O NO USUARIO CON ESTE CORREO')
            #SI EXISTE UN USUARIO CON EL CORREO DEL MENSAJE, ENTONCES
            if Usuario.objects.filter(correo=nuevo_mensaje.correo):
                print('EXISTE CORREO, ACTUALIZAR MENSAJE CON EL USUARIO EXISTENTE')
                print(Usuario.objects.filter(correo=nuevo_mensaje.correo).get())
                #VINCULO EL CORREO DEL MENSAJE CON EL CORREO DEL USUARIO EXISTENTE
                nuevo_mensaje.usuario = Usuario.objects.filter(correo=nuevo_mensaje.correo).get()
                nuevo_mensaje.save()
            #SINO NO EXISTE, CREO EL NUEVO USUARIO USANDO EL CORREO DEL MENSAJE
            else:

                nuevo_usuario = Usuario(correo=nuevo_mensaje.correo)
                nuevo_usuario.save()
                nuevo_mensaje.usuario = nuevo_usuario
                nuevo_mensaje.save()
                print(nuevo_usuario)



                
                # nuevo_mensaje.save()
                # nuevo_usuario = Usuario.objects.create(correo=nuevo_mensaje.correo)
                # nuevo_usuario.save()
                # nuevo_mensaje.usuario = nuevo_usuario
                # Mensaje.objects.filter(id=Mensaje.objects.filter(nuevo_mensaje.correo).value('id')).update(usuario=Usuario.objects.filter(correo=nuevo_mensaje.correo))

            return redirect('ecopuraApp:contacto_url')
        
        else:
            return render(request, self.template_name, {'form': form})

class ProductoView(TemplateView):
    template_name='productos.html'

class KitIniciales(ListView):
    template_name='kit-iniciales.html'
    model = Producto
    paginate_by = 9
    ordering= ['nombre']
    def get_queryset(self):
        return Producto.objects.filter(tipo_id = 2)

class DispAcces(ListView):
    template_name='dispacces.html'
    model = Producto
    paginate_by = 9
    ordering= ['nombre']
    def get_queryset(self):
        return Producto.objects.filter(tipo_id = 3)
    context_object_name = 'productos'

class Planes(CreateView):
    model = Mensaje
    template_name='planes.html'
    form_class = CrearContactoForm
    success_url= reverse_lazy('ecopuraApp:contacto_url')
    
    #Considerar que cuando llamo a la funcion post, tengo que sobre escribir
    #tanto si esta validando como el save.
    def post(self, request, *args, **kwargs):
        form =  self.form_class(request.POST)
        if form.is_valid():
            nuevo_mensaje = Mensaje(
                p_nombre = form.cleaned_data.get('p_nombre'),
                p_apellido = form.cleaned_data.get('p_apellido'),
                empresa = form.cleaned_data.get('empresa'),
                telefono = form.cleaned_data.get('telefono'),
                rut_empresa = form.cleaned_data.get('rut_empresa'),
                correo = form.cleaned_data.get('correo'),
                detalle_dispensador = form.cleaned_data.get('detalle_dispensador'),
                detalle_texto = form.cleaned_data.get('detalle_texto'),
                creacion = form.cleaned_data.get('creacion'),
            )
            cv = str(nuevo_mensaje.rut_empresa).partition('-')[2]
            nuevo_mensaje.rut_ver_empresa = cv
            print('He guardado el mensaje')
            print(nuevo_mensaje.correo)
            print('AHORA VERIFICO SI EXISTE O NO USUARIO CON ESTE CORREO')
            #SI EXISTE UN USUARIO CON EL CORREO DEL MENSAJE, ENTONCES
            if Usuario.objects.filter(correo=nuevo_mensaje.correo):
                print('EXISTE CORREO, ACTUALIZAR MENSAJE CON EL USUARIO EXISTENTE')
                print(Usuario.objects.filter(correo=nuevo_mensaje.correo).get())
                #VINCULO EL CORREO DEL MENSAJE CON EL CORREO DEL USUARIO EXISTENTE
                nuevo_mensaje.usuario = Usuario.objects.filter(correo=nuevo_mensaje.correo).get()
                nuevo_mensaje.save()
            #SINO NO EXISTE, CREO EL NUEVO USUARIO USANDO EL CORREO DEL MENSAJE
            else:

                nuevo_usuario = Usuario(correo=nuevo_mensaje.correo)
                nuevo_usuario.save()
                nuevo_mensaje.usuario = nuevo_usuario
                nuevo_mensaje.save()
                print(nuevo_usuario)



                
                # nuevo_mensaje.save()
                # nuevo_usuario = Usuario.objects.create(correo=nuevo_mensaje.correo)
                # nuevo_usuario.save()
                # nuevo_mensaje.usuario = nuevo_usuario
                # Mensaje.objects.filter(id=Mensaje.objects.filter(nuevo_mensaje.correo).value('id')).update(usuario=Usuario.objects.filter(correo=nuevo_mensaje.correo))

            return redirect('ecopuraApp:contacto_url')
        
        else:
            return render(request, self.template_name, {'form': form})



 #BORRAR ESTA CLASE QUE FUE USADA PARA CREAR LA LISTAX
class ListarTodosProductos(ListView):
    template_name='lista.html'
    paginate_by = 9
    model = Producto
    context_object_name = 'productos'

