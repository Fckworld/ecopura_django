from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import *

app_name = 'usuarios'
#APP_NAME ME SIRVE PARA PODER UTILIZAR EL REVERSE_LAZY, DICIENDOLE QUE APP VAMOS A USAR Y EL NOMBRE (name='contacto_url')
#DE LA URL A LA  QUE VAMOS REDIRECCIONAR
urlpatterns = [
    #PRIMER PARAMETRO PARA EL DIRECCIONAR CON URL, Y EL SEGUNDO ES EL NOMBRE DE LA FUNCION 
    #QUE ESTA EN LAS VISTAS (NO OLVIDAR IMPORTARLAS).
    path('',Registrar.as_view(),name='registrar_url'),
    path('registrado',RegistroExitoso.as_view(),name='registroexitoso_url'),
    path('login',IniciarSesion.as_view(),name='login_url'),
    path('logout',CerrarSesion.as_view(),name='logout_url')
    
]
