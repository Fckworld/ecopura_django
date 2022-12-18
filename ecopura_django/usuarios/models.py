from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.


class CustomAccountManager(BaseUserManager):
    # el nombre de los argumentos que recibe la funcion
    # create_user tienen que ser los mismos nombre que se usan
    # al declarar las variables utilizar en el modelo Usuario
    def create_superuser(self, correo, password, **other_fields):

        # ES OBLIGATORIO LOS VALORES IS_STAFF Y IS_SUPERUSER, ES OBVIO YA QUE ES LO QUE ESTAMOS CREANDO
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(correo, password, **other_fields)

    def create_user(self, correo, password, **other_fields):

        if not correo:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(correo)
        user = self.model(correo=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):

    # AL LLAMAR PERMISSIONMIXIN ESTE ME PERMITE CREAR LAS TABLAS DE GRUPO Y PERMISOS EN LA BASE DE DATOS AL MIGRAR

    # ADEMAS NO OLVIDAR QUE UN CORREO( PARA EL CAMPO USERNAME_FIELD) Y IS_STAFF SON OBLIGATORIOS EN ABSTRACTBASEUSER
    correo = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    #PERSONALIZACION
    rut = models.CharField(max_length=13, null = True, blank = True)
    cod_ver_rut = models.CharField(max_length=1, null = True, blank = True)
    rut_empresa = models.CharField(max_length=13, null = True, blank = True)
    cod_ver_empresa = models.CharField(max_length=1, null = True, blank = True)
    p_nombre = models.CharField(max_length=25, null = True, blank = True)
    s_nombre = models.CharField(max_length=25, null = True, blank = True)
    p_apellido = models.CharField(max_length=25, null = True, blank = True)
    s_apellido = models.CharField(max_length=25, null = True, blank = True)
    telefono = models.IntegerField(null=True, blank=True)

    #stime_of_day = models.DateTimeField(null=True)

    USERNAME_FIELD = 'correo'

    objects = CustomAccountManager()

    def __str__(self):
        return self.correo


@receiver(post_save, sender=Usuario)   
def dar_relacion_usuario_mensaje(sender, instance,created, **kwargs):

    from ecopuraApp.models import Mensaje
    correo = instance.correo
    # SI EXISTE UN MENSAJE CON EL MISMO CORREO DEL USUARIO:
    if created:
        if Mensaje.objects.filter(correo=correo):
            # OBTENGO EL USUARIO QUE QUIERO VINCULAR CON EL CORREO DEL MENSAJE
            #usuario_a_vincular = Usuario.objects.get(correo=correo)
            usuario_a_vincular = Usuario.objects.get(correo=correo)
            # GUARDO LOS MENSAJES EN UN VARIABLE
            mensajes = Mensaje.objects.filter(correo=correo)
            # ACTRUALIZO TODOS LOS MENSAJES QUE GUARDÉ, VINCULADO EL USUARIO A TODOS LOS MENSAJES
            mensajes.update(user=usuario_a_vincular)


