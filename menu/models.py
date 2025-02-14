from django.db import models
from establecimientos.models import Establecimiento    
from django.utils import timezone


class Establecimiento(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE, related_name='menus')  # Relación con Establecimiento

    def __str__(self):
        return self.nombre


class Plato(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del plato
    descripcion = models.TextField(blank=True, null=True)  # Descripción del plato
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del plato
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='platos', blank=True, null=True)  # Relación con el menú

    def __str__(self):
        return self.nombre
    

class MenuPlato(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    orden = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('menu', 'plato')

    def __str__(self):
        return f"{self.menu.nombre} - {self.plato.nombre}"
    
    
    
class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Completado', 'Completado'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')
    fecha_pedido = models.DateTimeField(auto_now_add=True)  # Fecha y hora del pedido
    mesa = models.CharField(max_length=50, blank=True, null=True)  # Campo para la mesa
    platos = models.ManyToManyField(Plato, through='PedidoPlato')  # Relación con los platos

    def __str__(self):
        return f"Pedido {self.id} - {self.estado}"

class PedidoPlato(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)  # Relación con Pedido
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)  # Relación con Plato
    cantidad = models.IntegerField(default=1)  # Cantidad de platos

    def __str__(self):
        return f"{self.cantidad} x {self.plato.nombre} (Pedido {self.pedido.id})"