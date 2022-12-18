from django.http import HttpResponse
from django.shortcuts import redirect

def permitir_usuario(roles_permitidos[]):
    def decorator(funcion_vista):
        def wrapper_func(request, *args, **kwargs):
            grupo = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in roles_permitidos:
                return funcion_vista(request, *args, **kwargs)
            else:
                return HttpResponse('no esta permitido entrar a esta vista')
        return wrapper_func
    return decorator