"""
Script para crear datos de prueba en el sistema de turismo
"""

import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'turismo_django.settings')
django.setup()

from turismo_django.models import Clientes, Destinos, Guias_Turisticos, Paquetes_Turisticos, Reservas

def crear_datos_prueba():
    print("Creando datos de prueba para el sistema de turismo...")
    
    # 1. Crear Destinos
    destinos_data = [
        {
            'ciudad_destino': 'Fusagasugá',
            'departamento': 'Cundinamarca',
            'descripcion': 'Ciudad jardín de Colombia, conocida por sus flores y clima templado',
            'clima': 'Templado',
            'actividades': 'Recorrido por fincas floricultoras, caminatas ecológicas, visita al mercado campesino'
        },
        {
            'ciudad_destino': 'Zipacón',
            'departamento': 'Cundinamarca',
            'descripcion': 'Pueblo colonial con arquitectura tradicional y paisajes montañosos',
            'clima': 'Frío',
            'actividades': 'Cabalgatas, fotografía de paisajes, turismo religioso'
        },
        {
            'ciudad_destino': 'Arbeláez',
            'departamento': 'Cundinamarca',
            'descripcion': 'Paraíso climático con temperatura promedio de 22°C',
            'clima': 'Cálido',
            'actividades': 'Deportes acuáticos, pesca deportiva, descanso y relax'
        },
        {
            'ciudad_destino': 'Pasca',
            'departamento': 'Cundinamarca',
            'descripcion': 'Sitio arqueológico con historia precolombina',
            'clima': 'Templado',
            'actividades': 'Visita al museo arqueológico, caminatas culturales'
        },
        {
            'ciudad_destino': 'Sibaté',
            'departamento': 'Cundinamarca',
            'descripcion': 'Centro agroindustrial con lagunas y paisajes naturales',
            'clima': 'Templado',
            'actividades': 'Pesca deportiva, turismo rural, avistamiento de aves'
        }
    ]
    
    for destino_data in destinos_data:
        destino, created = Destinos.objects.get_or_create(
            ciudad_destino=destino_data['ciudad_destino'],
            defaults=destino_data
        )
        if created:
            print(f"  - Destino creado: {destino.ciudad_destino}")
    
    # 2. Crear Guías Turísticos
    guias_data = [
        {
            'nombre_guia': 'Carlos Rodríguez',
            'cedula_guia': '12345678',
            'email': 'carlos.rodriguez@turismo.com',
            'telefono': '3211234567',
            'especialidad': 'Historia y Cultura',
            'anos_experiencia': 5,
            'idiomas': 'Español, Inglés',
            'certificado': True
        },
        {
            'nombre_guia': 'María García',
            'cedula_guia': '87654321',
            'email': 'maria.garcia@turismo.com',
            'telefono': '3209876543',
            'especialidad': 'Ecoturismo',
            'anos_experiencia': 3,
            'idiomas': 'Español, Francés',
            'certificado': True
        }
    ]
    
    for guia_data in guias_data:
        guia, created = Guias_Turisticos.objects.get_or_create(
            cedula_guia=guia_data['cedula_guia'],
            defaults=guia_data
        )
        if created:
            print(f"  - Guía creado: {guia.nombre_guia}")
    
    # 3. Crear Paquetes Turísticos
    destinos = Destinos.objects.all()
    guias = Guias_Turisticos.objects.all()
    
    paquetes_data = [
        {
            'nombre_paquete': 'Tour Floral Fusagasugá',
            'destino': destinos[0],  # Fusagasugá
            'guia': guias[0],
            'duracion_dias': 1,
            'precio': 150000,
            'incluye': 'Guía especializado, transporte, entrada a fincas, almuerzo típico',
            'no_incluye': 'Gastos personales, propinas',
            'capacidad_maxima': 20
        },
        {
            'nombre_paquete': 'Aventura Colonial Zipacón',
            'destino': destinos[1],  # Zipacón
            'guia': guias[0],
            'duracion_dias': 2,
            'precio': 280000,
            'incluye': 'Alojamiento, transporte, guía, todas las comidas',
            'no_incluye': 'Bebidas alcohólicas, souvenirs',
            'capacidad_maxima': 15
        },
        {
            'nombre_paquete': 'Paraíso Climático Arbeláez',
            'destino': destinos[2],  # Arbeláez
            'guia': guias[1],
            'duracion_dias': 3,
            'precio': 450000,
            'incluye': 'Transporte, alojamiento, actividades acuáticas, guía ecológico',
            'no_incluye': 'Equipo deportivo personal',
            'capacidad_maxima': 12
        }
    ]
    
    for paquete_data in paquetes_data:
        paquete, created = Paquetes_Turisticos.objects.get_or_create(
            nombre_paquete=paquete_data['nombre_paquete'],
            defaults=paquete_data
        )
        if created:
            print(f"  - Paquete creado: {paquete.nombre_paquete}")
    
    # 4. Crear Clientes
    clientes_data = [
        {
            'cedula': '111111111',
            'nombre_completo': 'Ana María López',
            'email': 'ana.lopez@email.com',
            'telefono': '3101111111'
        },
        {
            'cedula': '222222222',
            'nombre_completo': 'Juan Carlos Martínez',
            'email': 'juan.martinez@email.com',
            'telefono': '3152222222'
        },
        {
            'cedula': '333333333',
            'nombre_completo': 'Laura Sofía Díaz',
            'email': 'laura.diaz@email.com',
            'telefono': '3203333333'
        }
    ]
    
    for cliente_data in clientes_data:
        cliente, created = Clientes.objects.get_or_create(
            cedula=cliente_data['cedula'],
            defaults=cliente_data
        )
        if created:
            print(f"  - Cliente creado: {cliente.nombre_completo}")
    
    # 5. Crear algunas Reservas de ejemplo
    clientes = Clientes.objects.all()
    paquetes = Paquetes_Turisticos.objects.all()
    
    if len(clientes) >= 2 and len(paquetes) >= 2:
        from datetime import date, timedelta
        
        reservas_data = [
            {
                'cliente': clientes[0],
                'paquete': paquetes[0],
                'fecha_inicio_viaje': date.today() + timedelta(days=7),
                'fecha_fin_viaje': date.today() + timedelta(days=8),
                'numero_personas': 2,
                'precio_total': paquetes[0].precio * 2,
                'estado': 'CONFIRMADA',
                'observaciones': 'Cliente requiere atención especial para alergias'
            },
            {
                'cliente': clientes[1],
                'paquete': paquetes[1],
                'fecha_inicio_viaje': date.today() + timedelta(days=14),
                'fecha_fin_viaje': date.today() + timedelta(days=16),
                'numero_personas': 4,
                'precio_total': paquetes[1].precio * 4,
                'estado': 'PENDIENTE',
                'observaciones': 'Familia con niños pequeños'
            }
        ]
        
        for reserva_data in reservas_data:
            reserva, created = Reservas.objects.get_or_create(
                cliente=reserva_data['cliente'],
                paquete=reserva_data['paquete'],
                defaults=reserva_data
            )
            if created:
                print(f"  - Reserva creada: {reserva.id_reserva}")
    
    print("\n¡Datos de prueba creados exitosamente!")
    print(f"Total destinos: {Destinos.objects.count()}")
    print(f"Total guías: {Guias_Turisticos.objects.count()}")
    print(f"Total paquetes: {Paquetes_Turisticos.objects.count()}")
    print(f"Total clientes: {Clientes.objects.count()}")
    print(f"Total reservas: {Reservas.objects.count()}")

if __name__ == '__main__':
    crear_datos_prueba()
