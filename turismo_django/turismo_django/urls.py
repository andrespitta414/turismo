"""
turismo_django - URLs Configuration
Configuración de rutas para el sistema de turismo
"""

from django.urls import path
from . import views

urlpatterns = [
    # Página principal - Dashboard con Lista Circular
    path('', views.dashboard_turismo, name='dashboard_turismo'),
    
    # Rutas CRUD para Reservas
    path('reserva/crear/', views.crear_reserva, name='crear_reserva'),
    path('reserva/editar/<int:id_reserva>/', views.editar_reserva, name='editar_reserva'),
    path('reserva/eliminar/<int:id_reserva>/', views.eliminar_reserva, name='eliminar_reserva'),
    
    # Rutas para Clientes
    path('cliente/crear/', views.crear_cliente, name='crear_cliente'),
]
