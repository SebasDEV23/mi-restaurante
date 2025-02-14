from django.contrib import admin
from .models import Pedido, PedidoPlato, Plato, Menu

    # Configuración para Plato (inline en Menu)
class PlatoInline(admin.TabularInline):
    model = Plato
    extra = 1

# Configuración para Menu
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')  # Campos a mostrar
    search_fields = ('nombre',)  # Búsqueda por nombre
    inlines = [PlatoInline]  # Incluye los platos del menú

# Configuración para Plato
@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'menu')  # Campos a mostrar
    list_filter = ('menu',)  # Filtros por menú
    search_fields = ('nombre',)  # Búsqueda por nombre

# Configuración para PedidoPlato (inline en Pedido)
class PedidoPlatoInline(admin.TabularInline):
    model = PedidoPlato
    extra = 1

# Método personalizado para obtener la hora del pedido
def hora_pedido(obj):
    return obj.fecha_pedido.strftime('%H:%M')  # Formato de hora (HH:MM)
hora_pedido.short_description = 'Hora del Pedido'

# Método personalizado para obtener los platos del pedido
def platos_pedido(obj):
    return ", ".join([plato.nombre for plato in obj.platos.all()])
platos_pedido.short_description = 'Platos'

# Configuración para Pedido
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado', hora_pedido, 'mesa', platos_pedido, 'total_pedido')  # Campos a mostrar
    list_filter = ('estado', 'fecha_pedido')  # Filtros
    search_fields = ('id', 'estado', 'mesa')  # Búsqueda
    inlines = [PedidoPlatoInline]  # Incluye los platos del pedido

    # Método para calcular el total del pedido
    def total_pedido(self, obj):
        return sum(item.plato.precio * item.cantidad for item in obj.pedidoplato_set.all())
    total_pedido.short_description = 'Total del Pedido'