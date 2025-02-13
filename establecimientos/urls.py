from django.urls import path
from . import views

app_name = 'establecimientos'  # Importante para nombres de URL inversos

urlpatterns = [
    # URLs para la gestión de establecimientos
    path('establecimientos/', views.lista_establecimientos, name='lista_establecimientos'), # Lista todos los establecimientos
    path('establecimiento/nuevo/', views.crear_establecimiento, name='crear_establecimiento'), # Formulario para crear un establecimiento
    path('establecimiento/<int:pk>/', views.detalle_establecimiento, name='detalle_establecimiento'), # Detalle de un establecimiento específico
    path('establecimiento/<int:pk>/editar/', views.editar_establecimiento, name='editar_establecimiento'), # Formulario para editar un establecimiento
    path('establecimiento/<int:pk>/eliminar/', views.eliminar_establecimiento, name='eliminar_establecimiento'), # Confirmación para eliminar un establecimiento
]