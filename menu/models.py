from django.db import models
from establecimientos.models import Establecimiento    
from django.utils import timezone




class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)
    platos = models.ManyToManyField('Plato', through='MenuPlato') # Añadimos ManyToManyField

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=20, decimal_places=0, default=1000,)
    moneda = models.CharField(max_length=10, default='COP') 
    imagen = models.ImageField(null=True, blank=True, upload_to='platos/')
    categoria = models.CharField(max_length=100, null=True, blank=True)

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
    mesa = models.IntegerField(null=True, blank=True)
    platos = models.ManyToManyField(Plato, through='PedidoPlato')
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE, related_name='pedidos')
    hora_pedido = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('preparando', 'Preparando'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ], default='pendiente')

    def __str__(self):
        return f"Pedido #{self.id} - Mesa {self.mesa or 'Sin asignar'}"

    def tiempo_transcurrido(self):
        ahora = timezone.now()
        tiempo = ahora - self.hora_pedido
        return tiempo.total_seconds() // 60

class PedidoPlato(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    class Meta:
        unique_together = ('pedido', 'plato')

    def __str__(self):
        return f"{self.pedido} - {self.plato} x {self.cantidad}"