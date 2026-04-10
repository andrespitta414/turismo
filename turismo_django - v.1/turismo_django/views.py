"""
turismo_django - Views.py
CRUD y lógica backend con integración de lista circular manual
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Clientes, Destinos, Guias_Turisticos, Paquetes_Turisticos, Reservas
from django.contrib import messages
from django.core.paginator import Paginator
import datetime
from .logica import ListaCircularDestinos


# ==================== VISTA PRINCIPAL DASHBOARD ====================

def dashboard_turismo(request):
    """
    Vista principal del dashboard que integra la Lista Circular Manual
    para el carrusel de destinos y muestra las reservas existentes
    """
    # 1. Usamos la Lista Circular Manual para el carrusel de destinos
    lista_circular = ListaCircularDestinos()
    destinos_db = Destinos.objects.all()
    
    # Insertamos cada destino en la lista circular manual
    for destino in destinos_db:
        lista_circular.agregar(destino.ciudad_destino)
    
    # 2. Obtenemos el listado del modelo Reservas para el CRUD
    reservas = Reservas.objects.all().order_by('-fecha_reserva')
    
    # 3. Obtenemos datos para los formularios
    clientes = Clientes.objects.all()
    paquetes = Paquetes_Turisticos.objects.filter(activo=True)
    
    context = {
        'destinos_circular': lista_circular.listar(),
        'reservas': reservas,
        'clientes': clientes,
        'paquetes': paquetes,
        'total_destinos': destinos_db.count(),
        'total_reservas': reservas.count(),
        'total_clientes': clientes.count(),
    }
    
    return render(request, 'dashboard.html', context)


# ==================== VISTAS CRUD PARA RESERVAS ====================

def crear_reserva(request):
    """
    Vista para crear una nueva reserva
    """
    if request.method == 'POST':
        try:
            # Debug: Imprimir datos recibidos
            print(f"Datos de reserva recibidos: {request.POST}")
            
            cedula_cliente = request.POST.get('cedula_cliente')
            id_paquete = request.POST.get('id_paquete')
            fecha_inicio = request.POST.get('fecha_inicio')
            fecha_fin = request.POST.get('fecha_fin')
            numero_personas = request.POST.get('numero_personas')
            observaciones = request.POST.get('observaciones', '')
            
            print(f"Reserva - Cédula: {cedula_cliente}, Paquete: {id_paquete}, Personas: {numero_personas}")
            
            # Validaciones básicas
            if not all([cedula_cliente, id_paquete, fecha_inicio, fecha_fin, numero_personas]):
                messages.error(request, 'Todos los campos son obligatorios')
                return redirect('dashboard_turismo')
            
            # Verificar cliente existe
            try:
                cliente = Clientes.objects.get(cedula=cedula_cliente)
                print(f"Cliente encontrado: {cliente}")
            except Clientes.DoesNotExist:
                print(f"Cliente no encontrado con cédula: {cedula_cliente}")
                messages.error(request, f'El cliente con cédula {cedula_cliente} no existe')
                return redirect('dashboard_turismo')
            
            # Verificar paquete existe
            try:
                paquete = Paquetes_Turisticos.objects.get(id_paquete=id_paquete)
                print(f"Paquete encontrado: {paquete}")
            except Paquetes_Turisticos.DoesNotExist:
                print(f"Paquete no encontrado con ID: {id_paquete}")
                messages.error(request, 'El paquete seleccionado no existe')
                return redirect('dashboard_turismo')
            
            # Crear la reserva
            reserva = Reservas(
                cliente=cliente,
                paquete=paquete,
                fecha_inicio_viaje=fecha_inicio,
                fecha_fin_viaje=fecha_fin,
                numero_personas=int(numero_personas),
                precio_total=paquete.precio * int(numero_personas),
                observaciones=observaciones
            )
            reserva.save()
            
            print(f"Reserva creada: {reserva}")
            messages.success(request, f'Reserva #{reserva.id_reserva} creada exitosamente')
            return redirect('dashboard_turismo')
            
        except ValueError as e:
            print(f"Error de valor: {str(e)}")
            messages.error(request, f'Error en los datos: {str(e)}')
        except Exception as e:
            print(f"Error al crear reserva: {str(e)}")
            messages.error(request, f'Error al crear la reserva: {str(e)}')
    
    return redirect('dashboard_turismo')


def editar_reserva(request, id_reserva):
    """
    Vista para editar una reserva existente
    """
    reserva = get_object_or_404(Reservas, id_reserva=id_reserva)
    
    if request.method == 'POST':
        try:
            reserva.fecha_inicio_viaje = request.POST.get('fecha_inicio')
            reserva.fecha_fin_viaje = request.POST.get('fecha_fin')
            reserva.numero_personas = int(request.POST.get('numero_personas'))
            reserva.estado = request.POST.get('estado')
            reserva.observaciones = request.POST.get('observaciones', '')
            
            # Recalcular precio total
            reserva.precio_total = reserva.paquete.precio * reserva.numero_personas
            reserva.save()
            
            messages.success(request, 'Reserva actualizada exitosamente')
            return redirect('dashboard_turismo')
            
        except Exception as e:
            messages.error(request, f'Error al actualizar la reserva: {str(e)}')
    
    context = {
        'reserva': reserva,
        'clientes': Clientes.objects.all(),
        'paquetes': Paquetes_Turisticos.objects.filter(activo=True),
    }
    return render(request, 'editar_reserva.html', context)


def eliminar_reserva(request, id_reserva):
    """
    Vista para eliminar una reserva
    """
    reserva = get_object_or_404(Reservas, id_reserva=id_reserva)
    
    if request.method == 'POST':
        try:
            reserva.delete()
            messages.success(request, 'Reserva eliminada exitosamente')
        except Exception as e:
            messages.error(request, f'Error al eliminar la reserva: {str(e)}')
    
    return redirect('dashboard_turismo')


# ==================== VISTAS PARA CLIENTES ====================

def crear_cliente(request):
    """
    Vista para crear un nuevo cliente
    """
    if request.method == 'POST':
        try:
            # Debug: Imprimir datos recibidos
            print(f"Datos recibidos: {request.POST}")
            
            cedula = request.POST.get('cedula')
            nombre_completo = request.POST.get('nombre_completo')
            email = request.POST.get('email')
            telefono = request.POST.get('telefono', '')
            
            print(f"Cédula: {cedula}, Nombre: {nombre_completo}, Email: {email}")
            
            if not cedula or not nombre_completo or not email:
                messages.error(request, 'Todos los campos son obligatorios')
                return redirect('dashboard_turismo')
            
            # Verificar si el cliente ya existe
            if Clientes.objects.filter(cedula=cedula).exists():
                messages.error(request, 'Ya existe un cliente con esa cédula')
                return redirect('dashboard_turismo')
            
            cliente = Clientes(
                cedula=cedula,
                nombre_completo=nombre_completo,
                email=email,
                telefono=telefono
            )
            cliente.save()
            
            print(f"Cliente guardado: {cliente}")
            messages.success(request, f'Cliente {nombre_completo} creado exitosamente')
            return redirect('dashboard_turismo')
            
        except Exception as e:
            print(f"Error al crear cliente: {str(e)}")
            messages.error(request, f'Error al crear el cliente: {str(e)}')
    
    return redirect('dashboard_turismo')
