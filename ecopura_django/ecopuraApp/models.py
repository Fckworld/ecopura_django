from django.db import models
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from django.conf import settings
from django.dispatch import receiver
from usuarios.models import Usuario
from django import forms

from django_google_maps import fields as map_fields

"""
SI BORRO UNO DATO DE PLACE, AUTOMATICAMENTE, SE BORRARÀ UNO DE RESUTARUANTE,
Y POR ENDE, TAMBIE  UNO DE WAITER
"""
class Direccion(models.Model):
    comuna = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)#CAMBIAR ESTOS CAMPOS EN PRODUCCION
    numero = models.IntegerField(null=True)
    otro = models.CharField(max_length=300, null=True, blank= True)


    def __str__(self):
        return self.comuna

# class Usuario(models.Model):
#     correo = models.EmailField(unique=True)
#     creacion = models.DateTimeField(auto_now_add=True)
#     numero = models.CharField(max_length=30,null=True, blank = True)
#     direccion = models.ManyToManyField(Direccion, null = True, blank= True)
  
    
    
#     def __str__(self):
#         return self.correo

class Ubicacion(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null = True, blank = True)

class Mensaje(models.Model):
    p_nombre = models.CharField(max_length=100)
    p_apellido = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100, null = True, blank = True)
    telefono = models.IntegerField()
    rut_empresa = models.CharField(max_length=13, null = True, blank = True)
    rut_ver_empresa = models.CharField(max_length=1, null = True, blank = True)
    correo = models.EmailField()
    
    BASIC = 'BS'
    ELECTRIC = 'EL'
    AMBAS = 'AB'
    CHOICES = [
        (BASIC,'Básico'),
        (ELECTRIC,'Eléctrico'),
        (AMBAS,'Ambos',)
    ]
    detalle_dispensador = models.CharField(max_length=2, choices=CHOICES, default=BASIC,)
    detalle_texto = models.TextField(null = True)
    #usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null = True, blank = True)
    #CREACION NO SE MUESTRA EN ADMIN POR SER UN AUTO_NOW_ADD
    creacion = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     blank=True,
    #     null=True,
    # )
    user = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )


class Cliente(models.Model):
    p_nombre = models.CharField(max_length=100)
    p_apellido = models.CharField(max_length=100)
    s_apellido = models.CharField(max_length=100, null = True, blank= True)
    contrasenia = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.OneToOneField(
        Usuario,
        on_delete = models.CASCADE,
    )
    # def __str__(self):
    #     return self.p_nombre+self.p_apellido

class Pago(models.Model):
    medio = models.CharField(max_length=30)
    def __str__(self):
        return self.medio

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)


class Tipo(models.Model):
    nombre = models.CharField(max_length=30, null= True)


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=300)
    foto = models.ImageField(null = True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    tipo = models.ForeignKey(Tipo, on_delete = models.CASCADE, null= True)
    

class Carrito(models.Model):
    valor_carro = models.IntegerField()
    descuento = models.IntegerField()
    producto = models.ManyToManyField(Producto)


class Boleta(models.Model):
    impuesto = models.FloatField()
    valor_total = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pago = models.OneToOneField(
        Pago,
        on_delete = models.CASCADE,
        null=True
    )
    carrito = models.OneToOneField(
        Carrito,
        on_delete = models.CASCADE,
        null=True,
    )

    
class Contacto(models.Model):
    p_nombre = models.CharField(max_length=100)
    p_apellido = models.CharField(max_length=100)
    numero = models.CharField(max_length=30,null=True)
    empresa = models.CharField(max_length=100,null= True, blank=True)
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField(max_length=500)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    

@receiver(post_save, sender=Mensaje)
def dar_relacion_mensaje_usuario(sender,instance,created,**kwargs):
    print('SIGNAL DE MENSAJE')
    correo = instance.correo
    #SI EXISTE UN USUARIO CON EL MISMO CORREO DEL MENSAJE
    print(instance.user)
    if Usuario.objects.filter(correo=correo):
        if created:
            Mensaje.objects.update(user = Usuario.objects.get(correo=correo))
   

