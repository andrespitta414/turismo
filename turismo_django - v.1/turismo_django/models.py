"""
turismo_django - Models.py
Modelos de datos para el sistema de gestión turística de Fusagasugá
"""

from django.db import models
from django.core.validators import EmailValidator
import datetime


class Clientes(models.Model):
    cedula = models.CharField(max_length=20, unique=True, primary_key=True, verbose_name="Cédula")
    nombre_completo = models.CharField(max_length=100, verbose_name="Nombre Completo")
    email = models.EmailField(validators=[EmailValidator()], verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    
    class Meta:
        db_table = 'Clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return f"{self.nombre_completo} - {self.cedula}"


class Destinos(models.Model):
    id_destino = models.AutoField(primary_key=True, verbose_name="ID Destino")
    ciudad_destino = models.CharField(max_length=100, verbose_name="Ciudad Destino")
    departamento = models.CharField(max_length=50, verbose_name="Departamento")
    descripcion = models.TextField(verbose_name="Descripción")
    clima = models.CharField(max_length=50, verbose_name="Clima")
    actividades = models.TextField(verbose_name="Actividades Disponibles")
    imagen_url = models.URLField(blank=True, null=True, verbose_name="URL Imagen")
    
    class Meta:
        db_table = 'Destinos'
        verbose_name = 'Destino'
        verbose_name_plural = 'Destinos'
    
    def __str__(self):
        return self.ciudad_destino


class Guias_Turisticos(models.Model):
    id_guia = models.AutoField(primary_key=True, verbose_name="ID Guía")
    nombre_guia = models.CharField(max_length=100, verbose_name="Nombre del Guía")
    cedula_guia = models.CharField(max_length=20, unique=True, verbose_name="Cédula")
    email = models.EmailField(validators=[EmailValidator()], verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    especialidad = models.CharField(max_length=100, verbose_name="Especialidad")
    anos_experiencia = models.PositiveIntegerField(verbose_name="Años de Experiencia")
    idiomas = models.CharField(max_length=200, verbose_name="Idiomas")
    certificado = models.BooleanField(default=False, verbose_name="Certificado")
    
    class Meta:
        db_table = 'Guias_Turisticos'
        verbose_name = 'Guía Turístico'
        verbose_name_plural = 'Guías Turísticos'
    
    def __str__(self):
        return self.nombre_guia


class Paquetes_Turisticos(models.Model):
    id_paquete = models.AutoField(primary_key=True, verbose_name="ID Paquete")
    nombre_paquete = models.CharField(max_length=100, verbose_name="Nombre del Paquete")
    destino = models.ForeignKey(Destinos, on_delete=models.CASCADE, verbose_name="Destino")
    guia = models.ForeignKey(Guias_Turisticos, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Guía Asignado")
    duracion_dias = models.PositiveIntegerField(verbose_name="Duración (Días)")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    incluye = models.TextField(verbose_name="Incluye")
    no_incluye = models.TextField(verbose_name="No Incluye")
    capacidad_maxima = models.PositiveIntegerField(verbose_name="Capacidad Máxima")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    
    class Meta:
        db_table = 'Paquetes_Turisticos'
        verbose_name = 'Paquete Turístico'
        verbose_name_plural = 'Paquetes Turísticos'
    
    def __str__(self):
        return f"{self.nombre_paquete} - {self.destino.ciudad_destino}"


class Reservas(models.Model):
    id_reserva = models.AutoField(primary_key=True, verbose_name="ID Reserva")
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, verbose_name="Cliente")
    paquete = models.ForeignKey(Paquetes_Turisticos, on_delete=models.CASCADE, verbose_name="Paquete")
    fecha_reserva = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Reserva")
    fecha_inicio_viaje = models.DateField(verbose_name="Fecha Inicio Viaje")
    fecha_fin_viaje = models.DateField(verbose_name="Fecha Fin Viaje")
    numero_personas = models.PositiveIntegerField(verbose_name="Número de Personas")
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Total")
    estado = models.CharField(
        max_length=20,
        choices=[
            ('PENDIENTE', 'Pendiente'),
            ('CONFIRMADA', 'Confirmada'),
            ('CANCELADA', 'Cancelada'),
            ('COMPLETADA', 'Completada'),
        ],
        default='PENDIENTE',
        verbose_name="Estado"
    )
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones")
    
    class Meta:
        db_table = 'Reservas'
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
    
    def __str__(self):
        return f"Reserva {self.id_reserva} - {self.cliente.nombre_completo}"
