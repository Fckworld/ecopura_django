from unicodedata import name
from django.urls import path

from ecopuraApp.views import *
app_name= 'ecopuraApp'
#APP_NAME ME SIRVE PARA PODER UTILIZAR EL REVERSE_LAZY, DICIENDOLE QUE APP VAMOS A USAR Y EL NOMBRE (name='contacto_url')
#DE LA URL A LA  QUE VAMOS REDIRECCIONAR
urlpatterns = [
    #PRIMER PARAMETRO PARA EL DIRECCIONAR CON URL, Y EL SEGUNDO ES EL NOMBRE DE LA FUNCION 
    #QUE ESTA EN LAS VISTAS (NO OLVIDAR IMPORTARLAS).
    path('',Inicio.as_view(),name='inicio_url'),
    path('agua',Agua.as_view(),name='agua_url'),
    path('productos',Producto.as_view(),name='productos_url'),
    path('kitiniciales',KitIniciales.as_view(),name='kitiniciales_url'),
    path('planes',Planes.as_view(),name='planes_url'), 
    
]