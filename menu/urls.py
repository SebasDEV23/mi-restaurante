from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('restaurante/<int:pk>/', views.mostrar_menu, name='mostrar_menu'),
    path('agregar_pedido/<int:plato_id>/', views.agregar_pedido, name='agregar_pedido'), 
    path('pedidos_pendientes/', views.pedidos_pendientes, name='pedidos_pendientes'),
    path('marcar_como_finalizado/<int:pedido_id>/', views.marcar_como_finalizado, name='marcar_como_finalizado'),
    path('marcar_como_preparando/<int:pedido_id>/', views.marcar_como_preparando, name='marcar_como_preparando'),
    path('', views.pedidos_pendientes, name='pedidos_pendientes'),  # Página principal del admin
    path('cambiar_estado_pedido/<int:pedido_id>/', views.cambiar_estado_pedido, name='cambiar_estado_pedido'), 
    
]
