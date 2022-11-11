from django.contrib import admin
from ecopuraApp.models import *
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','correo','numero')
 
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
    list_display = ('id','nombre','categoria','tipo','foto')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id','p_nombre','p_apellido','numero')

class TipoAdmin(admin.ModelAdmin):
    list_display= ('id','nombre')
class MensajeAdmin(admin.ModelAdmin):
    list_display= ('id','correo','detalle_texto')
class UbicacionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Direccion,DireccionAdmin)
admin.site.register(Boleta,BoletaAdmin)
admin.site.register(Pago,PagoAdmin)
admin.site.register(Carrito,CarritoAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Contacto,ContactoAdmin)
admin.site.register(Tipo,TipoAdmin)
admin.site.register(Mensaje,MensajeAdmin)
admin.site.register(Ubicacion,UbicacionAdmin)

