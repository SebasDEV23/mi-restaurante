from django.shortcuts import render, get_object_or_404, redirect
from .models import Establecimiento
from .forms import EstablecimientoForm # Importamos el formulario
from django.contrib.auth.decorators import login_required # Importamos el decorador


def lista_establecimientos(request):
    establecimientos = Establecimiento.objects.all()
    return render(request, 'establecimientos/lista_establecimientos.html', {'establecimientos': establecimientos})

@login_required
def detalle_establecimiento(request, pk):
    establecimiento = get_object_or_404(Establecimiento, pk=pk)
    return render(request, 'establecimientos/detalle_establecimiento.html', {'establecimiento': establecimiento})

@login_required
def crear_establecimiento(request):
    if request.method == 'POST':
        form = EstablecimientoForm(request.POST, request.FILES) # Incluimos request.FILES para las imágenes
        if form.is_valid():
            establecimiento = form.save(commit=False)
            establecimiento.administrador = request.user  # Asignamos el usuario actual como administrador
            establecimiento.save()
            return redirect('establecimientos:detalle_establecimiento', pk=establecimiento.pk)
    else:
        form = EstablecimientoForm()
    return render(request, 'establecimientos/form_establecimiento.html', {'form': form})

@login_required
def editar_establecimiento(request, pk):
    establecimiento = get_object_or_404(Establecimiento, pk=pk)
    if establecimiento.administrador != request.user: # Solo el administrador puede editar
        return redirect('establecimientos:lista_establecimientos')
    if request.method == 'POST':
        form = EstablecimientoForm(request.POST, request.FILES, instance=establecimiento)
        if form.is_valid():
            form.save()
            return redirect('establecimientos:detalle_establecimiento', pk=establecimiento.pk)
    else:
        form = EstablecimientoForm(instance=establecimiento)
    return render(request, 'establecimientos/form_establecimiento.html', {'form': form})

@login_required
def eliminar_establecimiento(request, pk):
    establecimiento = get_object_or_404(Establecimiento, pk=pk)
    if establecimiento.administrador != request.user: # Solo el administrador puede eliminar
        return redirect('establecimientos:lista_establecimientos')
    if request.method == 'POST':
        establecimiento.delete()
        return redirect('establecimientos:lista_establecimientos')
    return render(request, 'establecimientos/eliminar_establecimiento.html', {'establecimiento': establecimiento})
