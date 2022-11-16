from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class AdministradorCuentaPersonalizado(BaseUserManager):
    def create_superuser(self,correo,nombre_usuario, primer_nombre, password, **otras_mierdas):
        otras_mierdas.setdefault('is_staff',True)
        otras_mierdas.setdefault('is_superuser',True)
        otras_mierdas.setdefault('is_activate',True)
        
        if otras_mierdas.get('is_staff') is not True:
            raise ValueError('Super usuario debe ser asignado a is_staff=True.')

        if otras_mierdas.get('is_superuser') is not True:
            raise ValueError('Super usuario debe ser asignado a is_superuser=True.')

        return self.create_user(correo,nombre_usuario,primer_nombre,password,**otras_mierdas)

    def create_user(self,correo,nombre_usuario, primer_nombre, password, **otras_mierdas):
        
        if not correo:
            raise ValueError(('Debe proporionar un correo electronico'))
        
        correo = self.normalize_email(correo)
        usuario = self.model(
            correo = correo,
            nombre_usuario = nombre_usuario,
            primer_nombre = primer_nombre,
            **otras_mierdas
        )
        usuario.set_password(password)
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):
    correo = models.EmailField(('email address'), unique=True)
    nombre_usuario = models.CharField(max_length=30, unique=True)
    creacion = models.DateTimeField(auto_now_add=True)
    primer_nombre = models.CharField(max_length=30, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_activate = models.BooleanField(default=False)

    object = AdministradorCuentaPersonalizado()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre_usuario','primer_nombre']

    def __str__(self):
        return self.nombre_usuario