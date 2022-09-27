from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

from ecopuraApp.models import *

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
class Planes(TemplateView):
    template_name='planes.html'
 #BORRAR ESTA CLASE QUE FUE USADA PARA CREAR LA LISTAX
class ListarTodosProductos(ListView):
    template_name='lista.html'
    paginate_by = 9
    model = Producto
    context_object_name = 'productos'
