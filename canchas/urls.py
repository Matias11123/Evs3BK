from django.urls import path
from . import views

app_name = 'canchas'

urlpatterns = [
    path('', views.catalogo_canchas, name='catalogo'),
    path('cancha/<int:pk>/', views.detalle_cancha, name='detalle_cancha'),
    path('crear/', views.crear_cancha, name='crear_cancha'),
    path('editar/<int:pk>/', views.editar_cancha, name='editar_cancha'),
    path('eliminar/<int:pk>/', views.eliminar_cancha, name='eliminar_cancha'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:pk>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/limpiar/', views.limpiar_carrito, name='limpiar_carrito'),
]