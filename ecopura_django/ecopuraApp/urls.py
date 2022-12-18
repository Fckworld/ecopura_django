from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout_then_login
from ecopuraApp.views import *
from usuarios.views import *


app_name= 'ecopuraApp'
#APP_NAME ME SIRVE PARA PODER UTILIZAR EL REVERSE_LAZY, DICIENDOLE QUE APP VAMOS A USAR Y EL NOMBRE (name='contacto_url')
#DE LA URL A LA  QUE VAMOS REDIRECCIONAR
urlpatterns = [
    #PRIMER PARAMETRO PARA EL DIRECCIONAR CON URL, Y EL SEGUNDO ES EL NOMBRE DE LA FUNCION 
    #QUE ESTA EN LAS VISTAS (NO OLVIDAR IMPORTARLAS).
    path('',Inicio.as_view(),name='inicio_url'),
    path('agua',Agua.as_view(),name='agua_url'),
    path('productos',ProductoView.as_view(),name='productos_url'),
    path('kitiniciales',KitIniciales.as_view(),name='kitiniciales_url'),
    path('planes',Planes.as_view(),name='planes_url'), 
    path('dispacces',DispAcces.as_view(),name='dispacces_url'),
    path('lista',ListarTodosProductos.as_view(),name='listartodosproductos_url'),
    path('detalle/<int:pk>',ProductoDetalle.as_view(),name='detalle_url'),
    path('contacto', CrearContacto.as_view(),name='contacto_url'),
    path('succesfull',Succesfull.as_view(),name='successfull_url'),
    path('preguntas-frecuentes',PreguntasFrecuentes.as_view(),name='preguntasfrecuentes_url'),
    path('politicas-despacho',PoliticasDespacho.as_view(),name='politicasdespacho_url'),
    path('garantia',Garantia.as_view(),name='garantia_url'),
    path('zona-despacho',ZonaDespacho.as_view(),name='zonadespacho_url'),
    path('tratamiendo-de-aguas',TratamientoAguas.as_view(),name = 'tratamientoaguas_url'),
    path('iniciar-sesion', InicioSesion.as_view(),name='iniciosesion_url'),
    ]

