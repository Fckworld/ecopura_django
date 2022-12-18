from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from usuarios.models import Usuario
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
    ordering= ['id']
    def get_queryset(self):
        return Producto.objects.filter(tipo_id = 1).order_by('nombre')

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
        print(form)
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
            
            # #SI EXISTE UN USUARIO CON EL CORREO DEL MENSAJE, ENTONCES
            # if Usuario.objects.filter(correo=nuevo_mensaje.correo):
            #     #VINCULO EL CORREO DEL MENSAJE CON EL CORREO DEL USUARIO EXISTENTE
            #     nuevo_mensaje.user = Usuario.objects.filter(correo=nuevo_mensaje.correo).get()
            # #SINO NO EXISTE, CREO EL NUEVO USUARIO USANDO EL CORREO DEL MENSAJE
            nuevo_mensaje.save()
            
            contenido_mensaje ='"'+nuevo_mensaje.p_nombre+' '+nuevo_mensaje.p_apellido+'" esta tratando de contactarnos, nos dice:'+'"'+nuevo_mensaje.detalle_texto+'"'
            
            send_mail(
                'CONTACTO ECOPURA',
                contenido_mensaje,
                'e5520aa04652f9',
                ['ecopurachilecontacto@ecopurachile.cl'],
                fail_silently=False,
            )

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
            #SACO EL CV
            cv = str(nuevo_mensaje.rut_empresa).partition('-')[2]
            #LO GUARDO EN SU CAMPO CORRESPONDIENTE
            nuevo_mensaje.rut_ver_empresa = cv

            #SI EXISTE UN USUARIO CON EL CORREO DEL MENSAJE, ENTONCES
            if Usuario.objects.filter(correo=nuevo_mensaje.correo):
                #VINCULO EL CORREO DEL MENSAJE CON EL CORREO DEL USUARIO EXISTENTE
                #EL USUARIO DE ESTE MENSAJE VA A SER EL USUARION QUE YA TIENE ESE CORREO REGISTADO.
                nuevo_mensaje.user = Usuario.objects.filter(correo=nuevo_mensaje.correo).get()
                #GUARDO EL MENSAJE EN BD CON USUARIO VINCULADO
            nuevo_mensaje.save()
 
            
            
            contenido_mensaje ='NOMBRE:'+nuevo_mensaje.p_nombre+' '+nuevo_mensaje.p_apellido+'. \n MENSAJE:'+nuevo_mensaje.detalle_texto+'.\nNUMERO DE CONTACTO:'+str(nuevo_mensaje.telefono)+'.\n EMPRESA:'+nuevo_mensaje.empresa+'.\n RUT EMPRESA:'+nuevo_mensaje.rut_empresa
            
            send_mail(
                'CONTACTO ECOPURA',
                contenido_mensaje,
                'e5520aa04652f9',
                ['ecopurachilecontacto@ecopurachile.cl'],
                fail_silently=False,
            )

            return redirect('ecopuraApp:successfull_url')
        
        #SI EL FORMULARIO NO PASA LAS VALIDACIONES, SE ACTUALIZA MOSTRANDO LOS ERRORES
        else:
            return render(request, self.template_name, {'form': form})



 #BORRAR ESTA CLASE QUE FUE USADA PARA CREAR LA LISTAX
class ListarTodosProductos(ListView):
    template_name='lista.html'
    paginate_by = 9
    model = Producto
    context_object_name = 'productos'

class Succesfull(TemplateView):
    template_name = 'sucessfull.html'

class PreguntasFrecuentes(TemplateView):
    template_name = 'preguntas-frecuentes.html'

class PoliticasDespacho(TemplateView):
    template_name = 'politicas-despacho.html'
class Garantia(TemplateView):
    template_name= 'garantia.html'
class ZonaDespacho(TemplateView):
    template_name='zona-despacho.html'
class TratamientoAguas(TemplateView):
    template_name='tratamiento-aguas.html'

class InicioSesion(TemplateView):
    template_name= 'inicio-sesion.html'