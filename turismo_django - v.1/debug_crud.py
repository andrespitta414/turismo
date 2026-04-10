#!/usr/bin/env python
"""
Script para depurar problemas de CRUD en el sistema de turismo
"""

import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'turismo_django.settings')
django.setup()

from turismo_django.models import Clientes, Destinos, Guias_Turisticos, Paquetes_Turisticos, Reservas

def debug_database():
    print("=== DEPURACIÓN DE BASE DE DATOS ===")
    
    # 1. Verificar clientes
    print(f"\n1. CLIENTES:")
    clientes = Clientes.objects.all()
    print(f"   Total clientes: {clientes.count()}")
    for cliente in clientes:
        print(f"   - {cliente.cedula}: {cliente.nombre_completo} ({cliente.email})")
    
    # 2. Verificar destinos
    print(f"\n2. DESTINOS:")
    destinos = Destinos.objects.all()
    print(f"   Total destinos: {destinos.count()}")
    for destino in destinos:
        print(f"   - {destino.ciudad_destino} ({destino.departamento})")
    
    # 3. Verificar guías
    print(f"\n3. GUÍAS:")
    guias = Guias_Turisticos.objects.all()
    print(f"   Total guías: {guias.count()}")
    for guia in guias:
        print(f"   - {guia.nombre_guia} ({guia.especialidad})")
    
    # 4. Verificar paquetes
    print(f"\n4. PAQUETES:")
    paquetes = Paquetes_Turisticos.objects.all()
    print(f"   Total paquetes: {paquetes.count()}")
    for paquete in paquetes:
        print(f"   - {paquete.nombre_paquete}: ${paquete.precio} (Activo: {paquete.activo})")
    
    # 5. Verificar reservas
    print(f"\n5. RESERVAS:")
    reservas = Reservas.objects.all()
    print(f"   Total reservas: {reservas.count()}")
    for reserva in reservas:
        print(f"   - #{reserva.id_reserva}: {reserva.cliente.nombre_completo} - {reserva.paquete.nombre_paquete} ({reserva.estado})")

def test_cliente_creation():
    print("\n=== TEST CREACIÓN DE CLIENTE ===")
    
    try:
        # Verificar si ya existe
        cedula_test = "999999999"
        if Clientes.objects.filter(cedula=cedula_test).exists():
            print(f"Cliente con cédula {cedula_test} ya existe")
            return
        
        # Crear cliente de prueba
        cliente = Clientes.objects.create(
            cedula=cedula_test,
            nombre_completo="Cliente de Prueba",
            email="test@ejemplo.com",
            telefono="3000000000"
        )
        print(f"Cliente creado exitosamente: {cliente}")
        
        # Verificar que se guardó
        cliente_guardado = Clientes.objects.get(cedula=cedula_test)
        print(f"Cliente verificado en BD: {cliente_guardado}")
        
    except Exception as e:
        print(f"Error al crear cliente: {str(e)}")

def test_reserva_creation():
    print("\n=== TEST CREACIÓN DE RESERVA ===")
    
    try:
        # Verificar que existan clientes y paquetes
        clientes = Clientes.objects.all()
        paquetes = Paquetes_Turisticos.objects.all()
        
        if not clientes.exists():
            print("No hay clientes para crear reserva")
            return
        
        if not paquetes.exists():
            print("No hay paquetes para crear reserva")
            return
        
        # Crear reserva de prueba
        cliente = clientes.first()
        paquete = paquetes.first()
        
        from datetime import date, timedelta
        reserva = Reservas.objects.create(
            cliente=cliente,
            paquete=paquete,
            fecha_inicio_viaje=date.today() + timedelta(days=7),
            fecha_fin_viaje=date.today() + timedelta(days=8),
            numero_personas=2,
            precio_total=paquete.precio * 2,
            estado='PENDIENTE',
            observaciones='Reserva de prueba'
        )
        print(f"Reserva creada exitosamente: #{reserva.id_reserva}")
        
        # Verificar que se guardó
        reserva_guardada = Reservas.objects.get(id_reserva=reserva.id_reserva)
        print(f"Reserva verificada en BD: {reserva_guardada}")
        
    except Exception as e:
        print(f"Error al crear reserva: {str(e)}")

if __name__ == '__main__':
    debug_database()
    test_cliente_creation()
    test_reserva_creation()
    print("\n=== DEPURACIÓN COMPLETADA ===")
