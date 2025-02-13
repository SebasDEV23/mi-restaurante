from django.contrib import admin
from .models import Establecimiento

@admin.register(Establecimiento)
class EstablecimientoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'administrador')
    search_fields = ('nombre', 'direccion')
    list_filter = ('administrador',) 