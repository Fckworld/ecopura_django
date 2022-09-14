from django.contrib import admin
from ecopuraApp.models import *

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','correo')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','p_nombre','s_apellido')

class DireccionAdmin(admin.ModelAdmin):
    list_display = ('id','comuna','direccion')

class BoletaAdmin(admin.ModelAdmin):
    list_display = ('id','impuesto')

class PagoAdmin(admin.ModelAdmin):
    list_display = ('id','medio')

class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id','valor_carro')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','precio','foto')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id','p_nombre','p_apellido','numero')

class KitAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')

class PromocionAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')


admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Direccion,DireccionAdmin)
admin.site.register(Boleta,BoletaAdmin)
admin.site.register(Pago,PagoAdmin)
admin.site.register(Carrito,CarritoAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Contacto,ContactoAdmin)
admin.site.register(Kit,KitAdmin)
admin.site.register(Promocion,PromocionAdmin)

