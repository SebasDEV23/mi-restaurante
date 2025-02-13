from django.shortcuts import render, redirect, get_object_or_404
from .models import Establecimiento, Menu, Plato, MenuPlato, Pedido, PedidoPlato
from django.db.models import Prefetch
from django.http import HttpResponseBadRequest
from django.contrib import messages
from django.utils import timezone



def mostrar_menu(request, pk):
    establecimiento = get_object_or_404(Establecimiento, pk=pk)

    menus = Menu.objects.filter(establecimiento=establecimiento).prefetch_related(
        Prefetch('menuplato_set', queryset=MenuPlato.objects.order_by('orden'))
    )

    context = {'establecimiento': establecimiento, 'menus': menus}
    return render(request, 'menu/mostrar_menu.html', context)


def agregar_pedido(request, plato_id):  # Nueva vista para agregar pedido
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        mesa = int(request.POST.get('mesa'))  # Obtén el número de mesa
        establecimiento_id = request.POST.get('establecimiento_id')

        if not mesa:
            return HttpResponseBadRequest("Debes seleccionar un número de mesa.")

        pedido = Pedido.objects.create(
            mesa=mesa,
            establecimiento_id=establecimiento_id
        )

        plato = get_object_or_404(Plato, pk=plato_id)
        PedidoPlato.objects.create(pedido=pedido, plato=plato, cantidad=cantidad)
        messages.success(request, "¡Pedido realizado!")
        return redirect('menu:mostrar_menu', pk=establecimiento_id)  # Redirige a la página del menú
    return HttpResponseBadRequest("Método no permitido.")



def pedidos_pendientes(request):
    pedidos = Pedido.objects.filter(estado='pendiente').order_by('hora_pedido').prefetch_related(
        'platos',  # Obtén los platos relacionados
        'pedidoplato_set'  # Obtén las cantidades relacionadas
    )
    return render(request, 'menu/pedidos_pendientes.html', {'pedidos': pedidos})




def marcar_como_finalizado(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    pedido.estado = 'entregado'  # Cambiar el estado a 'entregado'
    pedido.save()
    return redirect('menu:pedidos_pendientes')



def marcar_como_preparando(request, pedido_id):  # Nueva vista para "En preparación"
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    pedido.estado = 'preparando'
    pedido.save()
    return redirect('menu:pedidos_pendientes')

def cambiar_estado_pedido(request, pedido_id):  # Nueva vista para cambiar el estado
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        pedido.estado = nuevo_estado
        pedido.save()
    return redirect('menu:pedidos_pendientes')



