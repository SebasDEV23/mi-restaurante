from django.contrib import admin
from .models import Menu, Plato, MenuPlato 
from .models import Pedido, PedidoPlato


class MenuPlatoInline(admin.TabularInline): # usado para el orden
    model = MenuPlato
    extra = 1

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'establecimiento')
    inlines = [MenuPlatoInline]  # Usado para inlines para MenuPlato
    search_fields = ('nombre',)
    list_filter = ('establecimiento',)

@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('categoria',)
    


class PedidoPlatoInline(admin.TabularInline):
    model = PedidoPlato
    extra = 0

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'mesa', 'hora_pedido', 'estado', 'establecimiento')
    list_filter = ('estado', 'establecimiento')
    inlines = [PedidoPlatoInline]
    readonly_fields = ('hora_pedido',)  # No permitir editar la hora del pedido

    def tiempo_transcurrido(self, obj):  # Método para mostrar tiempo transcurrido en el admin
        return f"{obj.tiempo_transcurrido()} minutos"
    tiempo_transcurrido.short_description = "Tiempo transcurrido"
    tiempo_transcurrido.admin_order_field = 'hora_pedido'  # Ordenar por hora de pedido