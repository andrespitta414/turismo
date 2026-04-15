#!/usr/bin/env python
"""
Script para crear manualmente las tablas de la base de datos
"""

import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'turismo_django.settings')
django.setup()

from django.db import connection

def drop_tables():
    """Eliminar las tablas existentes"""
    
    sql_statements = [
        "DROP TABLE IF EXISTS Reservas",
        "DROP TABLE IF EXISTS Paquetes_Turisticos",
        "DROP TABLE IF EXISTS Guias_Turisticos",
        "DROP TABLE IF EXISTS Destinos",
        "DROP TABLE IF EXISTS Clientes"
    ]
    
    with connection.cursor() as cursor:
        for sql in sql_statements:
            try:
                cursor.execute(sql)
                print(f"Tabla eliminada: {sql}")
            except Exception as e:
                print(f"Error eliminando tabla: {str(e)}")
        
        connection.commit()
        print("\n=== TABLAS ELIMINADAS ===")

def create_tables():
    """Crear las tablas manualmente usando SQL"""
    
    sql_statements = [
        # Tabla Clientes
        """
        CREATE TABLE IF NOT EXISTS Clientes (
            cedula VARCHAR(20) PRIMARY KEY,
            nombre_completo VARCHAR(100) NOT NULL,
            email VARCHAR(254) NOT NULL,
            telefono VARCHAR(15),
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        
        # Tabla Destinos
        """
        CREATE TABLE IF NOT EXISTS Destinos (
            id_destino INTEGER PRIMARY KEY AUTOINCREMENT,
            ciudad_destino VARCHAR(100) NOT NULL,
            departamento VARCHAR(50) NOT NULL,
            descripcion TEXT NOT NULL,
            clima VARCHAR(50),
            actividades TEXT,
            imagen_url VARCHAR(500)
        )
        """,
        
        # Tabla Guias_Turisticos
        """
        CREATE TABLE IF NOT EXISTS Guias_Turisticos (
            id_guia INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_guia VARCHAR(100) NOT NULL,
            cedula_guia VARCHAR(20) UNIQUE NOT NULL,
            email VARCHAR(254) NOT NULL,
            telefono VARCHAR(15) NOT NULL,
            especialidad VARCHAR(100),
            anos_experiencia INTEGER,
            idiomas VARCHAR(200),
            certificado BOOLEAN DEFAULT 0
        )
        """,
        
        # Tabla Paquetes_Turisticos
        """
        CREATE TABLE IF NOT EXISTS Paquetes_Turisticos (
            id_paquete INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_paquete VARCHAR(100) NOT NULL,
            destino_id INTEGER NOT NULL,
            guia_id INTEGER,
            duracion_dias INTEGER NOT NULL,
            precio DECIMAL(10,2) NOT NULL,
            incluye TEXT NOT NULL,
            no_incluye TEXT NOT NULL,
            capacidad_maxima INTEGER NOT NULL,
            activo BOOLEAN DEFAULT 1,
            FOREIGN KEY (destino_id) REFERENCES Destinos(id_destino),
            FOREIGN KEY (guia_id) REFERENCES Guias_Turisticos(id_guia)
        )
        """,
        
        # Tabla Reservas
        """
        CREATE TABLE IF NOT EXISTS Reservas (
            id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id VARCHAR(20) NOT NULL,
            paquete_id INTEGER NOT NULL,
            fecha_reserva TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            fecha_inicio_viaje DATE NOT NULL,
            fecha_fin_viaje DATE NOT NULL,
            numero_personas INTEGER NOT NULL,
            precio_total DECIMAL(10,2) NOT NULL,
            estado VARCHAR(20) DEFAULT 'PENDIENTE',
            observaciones TEXT,
            FOREIGN KEY (cliente_id) REFERENCES Clientes(cedula),
            FOREIGN KEY (paquete_id) REFERENCES Paquetes_Turisticos(id_paquete)
        )
        """
    ]
    
    with connection.cursor() as cursor:
        for i, sql in enumerate(sql_statements, 1):
            try:
                print(f"Ejecutando SQL {i}...")
                cursor.execute(sql)
                print(f"  Tabla creada exitosamente")
            except Exception as e:
                print(f"  Error creando tabla: {str(e)}")
        
        connection.commit()
        print("\n=== TABLAS CREADAS EXITOSAMENTE ===")

if __name__ == '__main__':
    drop_tables()
    create_tables()
