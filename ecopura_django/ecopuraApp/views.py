from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

from ecopuraApp.models import *

# Create your views here.

class Inicio(ListView):
    template_name= 'inicio.html'
    paginate_by = 9
    def get_queryset(self):
        try:
            return Producto.objects.all().values_list('id','nombre','precio','descripcion').union(Kit.objects.all().values_list('id','nombre','precio','descripcion')).union(Promocion.objects.all().values_list('id','nombre','precio','descripcion'))
        except:
            return print('error')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ala'] = 3
        return context

class Agua(TemplateView):
    template_name='agua.html'
class ProductoView(TemplateView):
    template_name='productos.html'
class KitIniciales(TemplateView):
    template_name='kit-iniciales.html'
class Planes(TemplateView):
    template_name='planes.html'

class ListarTodosProductos(ListView):
    template_name='lista_todos_productos.html'
    paginate_by = 9
    model = Producto
    context_object_name = 'productos'

class ProductoDetalle(DetailView):
    def get_queryset(self):
        try:
            return 0
        except:
            return 0
