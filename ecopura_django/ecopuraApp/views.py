from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from ecopuraApp.models import *

# Create your views here.

class Inicio(TemplateView):
    template_name= 'inicio.html'
class Agua(TemplateView):
    template_name='agua.html'
class ProductoView(TemplateView):
    template_name='productos.html'
class KitIniciales(TemplateView):
    template_name='kit-iniciales.html'
class Planes(TemplateView):
    template_name='planes.html'

class ListarTodosProductos(ListView):
    model = Producto
    template_name='lista_todos_productos.html'
    context_object_name = 'productos'
    ordering = ['id']