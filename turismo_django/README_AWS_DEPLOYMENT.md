# Despliegue Gratuito en AWS - Sistema de Turismo Django

## Resumen de Configuración
Este proyecto está configurado para desplegarse en AWS Elastic Beanstalk usando el Free Tier.

## Archivos de Configuración Creados
- `requirements.txt` - Dependencias del proyecto
- `.ebextensions/django.config` - Configuración de Elastic Beanstalk
- `wsgi.py` - Configuración WSGI para producción
- `application.py` - Configuración de aplicación

## Pasos para Despliegue en AWS

### 1. Instalar AWS CLI y EB CLI
```bash
pip install awscli awsebcli
```

### 2. Configurar Credenciales AWS
```bash
aws configure
# Ingresa tu Access Key ID y Secret Access Key
```

### 3. Inicializar Elastic Beanstalk
```bash
eb init -p python-3.9 turismo-django
```

### 4. Crear Entorno
```bash
eb create production
```

### 5. Desplegar Cambios
```bash
eb deploy
```

## Configuración de Base de Datos

### Opción 1: PostgreSQL en AWS RDS (Free Tier)
1. Ve a la consola de AWS RDS
2. Crea una instancia PostgreSQL
3. Configura las variables de entorno en Elastic Beanstalk:
   - RDS_DB_NAME: nombre de la base de datos
   - RDS_USERNAME: usuario de la base de datos
   - RDS_PASSWORD: contraseña
   - RDS_HOSTNAME: endpoint de RDS
   - RDS_PORT: 5432

### Opción 2: SQLite (Para desarrollo/testing)
El sistema automáticamente usará SQLite si no detecta variables de entorno RDS.

## Variables de Entorno Adicionales
Configura en Elastic Beanstalk:
- DJANGO_DEBUG: False
- DJANGO_ALLOWED_HOSTS: tu-dominio.elasticbeanstalk.com
- DJANGO_SECRET_KEY: genera una nueva clave secreta

## Costos (Free Tier)
- **Elastic Beanstalk**: 750 horas/mes gratis
- **RDS**: 750 horas/mes gratis (db.t2.micro)
- **S3**: 5 GB de almacenamiento gratis
- **Transferencia de datos**: 15 GB/mes gratis

## Comandos Útiles
```bash
# Ver estado del entorno
eb status

# Ver logs
eb logs

# Abrir aplicación en navegador
eb open

# Escalar entorno
eb scale 1
```

## Estructura del Proyecto para AWS
```
turismo_django/
|-- turismo_django/
|   |-- settings.py (configurado para producción)
|   |-- wsgi.py
|   |-- models.py
|   |-- views.py
|   |-- urls.py
|   |-- logica.py
|-- templates/
|   |-- dashboard.html
|-- requirements.txt
|-- .ebextensions/
|   |-- django.config
|-- application.py
|-- manage.py
```

## Notas Importantes
- El proyecto está configurado para detectar automáticamente si está en producción o desarrollo
- La Lista Circular Manual funciona igual en producción
- Las migraciones se ejecutan automáticamente en el despliegue
- Los archivos estáticos se sirven correctamente

## Soporte
Para problemas de despliegue, revisa los logs con `eb logs` o contacta al soporte de AWS.
