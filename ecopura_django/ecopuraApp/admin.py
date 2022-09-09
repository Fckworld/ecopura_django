from django.contrib import admin
from ecopuraApp.models import Place, Restaurant, Waiter

# Register your models here.
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id','name','address')

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('place','serves_hot_dogs','serves_pizza')


class WaiterAdmin(admin.ModelAdmin):
    list_display = ('id','restaurant','name')

admin.site.register(Place,PlaceAdmin)
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Waiter,WaiterAdmin)