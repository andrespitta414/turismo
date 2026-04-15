# Configuración AWS CLI - Guía Rápida

## Comandos para Configurar Credenciales

### 1. Abrir PowerShell como Administrador
- Click derecho en PowerShell → "Run as Administrator"

### 2. Configurar AWS CLI
```powershell
& "C:\Users\Andres\AppData\Local\Python\pythoncore-3.14-64\Scripts\aws.cmd" configure
```

### 3. Ingresa tus credenciales cuando te solicite:
```
AWS Access Key ID [None]: AKIAxxxxxxxxxxxxxxx
AWS Secret Access Key [None]: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Default region name [None]: us-east-1
Default output format [None]: json
```

### 4. Verificar Configuración
```powershell
& "C:\Users\Andres\AppData\Local\Python\pythoncore-3.14-64\Scripts\aws.cmd" s3 ls
```

## Comandos para Despliegue

### 1. Inicializar Elastic Beanstalk
```powershell
cd "c:\Users\Andres\Desktop\Personal\Universidad de Cundinamarca\IV Semestre\Estructuras de información\turismo_django"
& "C:\Users\Andres\AppData\Local\Python\pythoncore-3.14-64\Scripts\eb.exe" init -p python-3.9 turismo-django
```

### 2. Crear Entorno de Producción
```powershell
& "C:\Users\Andres\AppData\Local\Python\pythoncore-3.14-64\Scripts\eb.exe" create production
```

### 3. Desplegar Cambios
```powershell
& "C:\Users\Andres\AppData\Local\Python\pythoncore-3.14-64\Scripts\eb.exe" deploy
```

### 4. Abrir Aplicación
```powershell
& "C:\Users\Andres\AppData\Local\Python\pythoncore-3.14-64\Scripts\eb.exe" open
```

## Variables de Entorno para Producción

Después del despliegue, configura en AWS Console → Elastic Beanstalk → Configuration → Environment properties:

```
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=tu-app.elasticbeanstalk.com
DJANGO_SECRET_KEY=tu-clave-secreta-generada
RDS_DB_NAME=turismo_db
RDS_USERNAME=postgres
RDS_PASSWORD=tu-contraseña
RDS_HOSTNAME=tu-rds-endpoint.rds.amazonaws.com
RDS_PORT=5432
```

## Generar Secret Key
```powershell
python -c "import secrets; print(secrets.token_urlsafe(50))"
```
