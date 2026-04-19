#!/usr/bin/env python
"""
Script para verificar y crear datos de prueba
"""

import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'turismo_django.settings')
django.setup()

from turismo_django.models import Clientes, Destinos, Guias_Turisticos, Paquetes_Turisticos, Reservas
from django.db import connection

def check_tables():
    """Verificar si las tablas existen"""
    print("=== VERIFICANDO TABLAS ===")
    
    tables = [
        'Clientes',
        'Destinos', 
        'Guias_Turisticos',
        'Paquetes_Turisticos',
        'Reservas'
    ]
    
    with connection.cursor() as cursor:
        for table in tables:
            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")
            result = cursor.fetchone()
            if result:
                print(f"  Tabla '{table}' existe")
            else:
                print(f"  Tabla '{table}' NO existe")

def create_test_data():
    """Crear datos de prueba si no existen"""
    print("\n=== CREANDO DATOS DE PRUEBA ===")
    
    try:
        # Crear destinos
        if Destinos.objects.count() == 0:
            print("Creando destinos...")
            destinos_data = [
                ('Fusagasugá', 'Cundinamarca', 'Capital floral de Colombia', 'Clima templado', 'Jardines, fincas florales, senderismo'),
                ('Zipacón', 'Cundinamarca', 'Pueblo colonial', 'Clima templado', 'Arquitectura tradicional, paisajes campestres'),
                ('Arbeláez', 'Cundinamarca', 'Tierra de aguas', 'Clima cálido', 'Fuentes termales, naturaleza, ecoturismo'),
                ('Pasca', 'Cundinamarca', 'Cuna de artistas', 'Clima templado', 'Cultura, artesanías, museos'),
                ('Sibaté', 'Cundinamarca', 'Valle verde', 'Clima templado', 'Agricultura, paisajes campestres, gastronomía')
            ]
            
            for ciudad, dept, desc, clima, actividades in destinos_data:
                Destinos.objects.create(
                    ciudad_destino=ciudad,
                    departamento=dept,
                    descripcion=desc,
                    clima=clima,
                    actividades=actividades
                )
            print("  5 destinos creados")
        else:
            print(f"  Ya existen {Destinos.objects.count()} destinos")
        
        # Crear guías
        if Guias_Turisticos.objects.count() == 0:
            print("Creando guías...")
            Guias_Turisticos.objects.create(
                nombre_guia='Carlos Rodríguez',
                cedula_guia='123456789',
                especialidad='Historia y Cultura',
                telefono='3001234567',
                email='carlos.guia@email.com',
                anos_experiencia=5,
                idiomas='Español, Inglés',
                certificado=True
            )
            print("  1 guía creado")
        else:
            print(f"  Ya existen {Guias_Turisticos.objects.count()} guías")
        
        # Crear paquetes
        if Paquetes_Turisticos.objects.count() == 0:
            print("Creando paquetes...")
            destino = Destinos.objects.first()
            guia = Guias_Turisticos.objects.first()
            
            Paquetes_Turisticos.objects.create(
                nombre_paquete='Tour Floral Fusagasugá',
                destino=destino,
                guia=guia,
                duracion_dias=1,
                precio=150000,
                incluye='Transporte, entrada a jardines, guía turístico',
                no_incluye='Almuerzo, compras personales',
                capacidad_maxima=20,
                activo=True
            )
            print("  1 paquete creado")
        else:
            print(f"  Ya existen {Paquetes_Turisticos.objects.count()} paquetes")
        
        # Crear clientes
        if Clientes.objects.count() == 0:
            print("Creando clientes...")
            clientes_data = [
                ('111111111', 'Ana María López', 'ana.lopez@email.com', '3101111111'),
                ('222222222', 'Juan Carlos Martínez', 'juan.martinez@email.com', '3202222222'),
                ('1070464757', 'Andres Pitta', 'andrespitta7@gmail.com', '3153333333')
            ]
            
            for cedula, nombre, email, tel in clientes_data:
                Clientes.objects.create(
                    cedula=cedula,
                    nombre_completo=nombre,
                    email=email,
                    telefono=tel
                )
            print("  3 clientes creados")
        else:
            print(f"  Ya existen {Clientes.objects.count()} clientes")
        
        # Crear reservas
        if Reservas.objects.count() == 0:
            print("Creando reservas...")
            from datetime import date, timedelta
            
            cliente = Clientes.objects.first()
            paquete = Paquetes_Turisticos.objects.first()
            
            Reservas.objects.create(
                cliente=cliente,
                paquete=paquete,
                fecha_inicio_viaje=date.today() + timedelta(days=7),
                fecha_fin_viaje=date.today() + timedelta(days=8),
                numero_personas=2,
                precio_total=paquete.precio * 2,
                estado='PENDIENTE',
                observaciones='Reserva de prueba del sistema'
            )
            print("  1 reserva creada")
        else:
            print(f"  Ya existen {Reservas.objects.count()} reservas")
            
    except Exception as e:
        print(f"Error creando datos: {str(e)}")

def show_data():
    """Mostrar datos actuales"""
    print("\n=== DATOS ACTUALES ===")
    
    try:
        print(f"Clientes: {Clientes.objects.count()}")
        for c in Clientes.objects.all():
            print(f"  - {c.cedula}: {c.nombre_completo}")
        
        print(f"\nDestinos: {Destinos.objects.count()}")
        for d in Destinos.objects.all():
            print(f"  - {d.ciudad_destino} ({d.departamento})")
        
        print(f"\nReservas: {Reservas.objects.count()}")
        for r in Reservas.objects.all():
            print(f"  - #{r.id_reserva}: {r.cliente.nombre_completo} - {r.paquete.nombre_paquete}")
            
    except Exception as e:
        print(f"Error mostrando datos: {str(e)}")

if __name__ == '__main__':
    check_tables()
    create_test_data()
    show_data()
    print("\n=== VERIFICACIÓN COMPLETADA ===")
