from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect


def root_redirect(request): #Función para redireccionar
    return redirect('establecimientos:lista_establecimientos') #Redirecciona a la url con nombre 'lista_establecimientos'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('establecimientos/', include('establecimientos.urls')),
    path('', root_redirect, name='root'), #URL raiz
    path('', include('menu.urls')), # Incluye las URLs de la app menu
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
