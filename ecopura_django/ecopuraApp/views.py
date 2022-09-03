from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class Inicio(TemplateView):
    template_name= 'inicio.html'
class Agua(TemplateView):
    template_name='agua.html'
class Producto(TemplateView):
    template_name='productos.html'