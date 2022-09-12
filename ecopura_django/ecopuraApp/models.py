from django.db import models
"""
SI BORRO UNO DATO DE PLACE, AUTOMATICAMENTE, SE BORRARÀ UNO DE RESUTARUANTE,
Y POR ENDE, TAMBIE  UNO DE WAITER
"""

class Usuario(models.Model):
    correo = models.EmailField(null=False, unique=True)
    creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.correo

class Cliente(models.Model):
    p_nombre = models.CharField(max_length=30, null=False)
    p_apellido = models.CharField(max_length=30, null = False)
    s_apellido = models.CharField(max_length=30, null = False)
    contrasenia = models.CharField(max_length=30, null=False)
    creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.OneToOneField(
        Usuario,
        on_delete = models.CASCADE,
    )
    def __str__(self):
        return self.p_nombre+self.p_apellido


class Direccion(models.Model):
    comuna = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=50)#CAMBIAR ESTOS CAMPOS EN PRODUCCION
    numero = models.IntegerField()
    otro = models.CharField(max_length=300)
    clientes = models.ManyToManyField(Usuario)

    def __str__(self):
        return self.comuna

class Boleta(models.Model):
    impuesto = models.FloatField()
    valor_total = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Pago(models.Model):
    medio = models.CharField(max_length=30)
    boleta = models.OneToOneField(
        Boleta,
        on_delete = models.CASCADE,
    )

class Carrito(models.Model):
    valor_carro = models.IntegerField()
    descuento = models.IntegerField()
    boleta = models.OneToOneField(
        Boleta,
        on_delete = models.CASCADE,
    )

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)