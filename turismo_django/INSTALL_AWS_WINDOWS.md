# Instalación AWS CLI y Elastic Beanstalk en Windows

## Método 1: Instalación Automática (Recomendado)

### 1. Descargar AWS CLI
1. Ve a: https://aws.amazon.com/es/cli/
2. Descarga "AWS CLI MSI Installer para Windows (64-bit)"
3. Ejecuta el instalador y sigue las instrucciones

### 2. Verificar Instalación
Abre una nueva terminal (PowerShell) y ejecuta:
```powershell
aws --version
```

### 3. Instalar Elastic Beanstalk CLI
```powershell
pip install awsebcli
```

### 4. Verificar Instalación EB CLI
```powershell
eb --version
```

## Método 2: Usando Chocolatey (Si lo tienes instalado)
```powershell
choco install awscli
pip install awsebcli
```

## Método 3: Usando pip (Alternativa)
```powershell
pip install awscli
pip install awsebcli
```

## Configurar Credenciales AWS

### 1. Crear Cuenta AWS (si no tienes)
1. Ve a https://aws.amazon.com/es/
2. Crea una cuenta nueva (Free Tier incluido)
3. Ingresa datos de tarjeta (no te cobrarán en el Free Tier)

### 2. Obtener Credenciales
1. Inicia sesión en AWS Console
2. Ve a "My Security Credentials"
3. Crea "Access Keys"
4. Guarda el Access Key ID y Secret Access Key

### 3. Configurar en Terminal
```powershell
aws configure
```
Ingresa cuando te solicite:
- Access Key ID: [tu-access-key]
- Secret Access Key: [tu-secret-key]
- Default region: us-east-1
- Default output format: json

## Probar Configuración
```powershell
aws s3 ls
```

## Desplegar Proyecto
Una vez configurado:
```powershell
cd "c:\Users\Andres\Desktop\Personal\Universidad de Cundinamarca\IV Semestre\Estructuras de información\turismo_django"
eb init -p python-3.9 turismo-django
eb create production
```

## Problemas Comunes

### "aws no reconocido"
- Cierra y vuelve a abrir PowerShell
- Reinicia la computadora si persiste

### "pip no reconocido"
- Asegúrate de tener Python instalado
- Agrega Python a PATH del sistema

### Permisos
- Ejecuta PowerShell como Administrador

## Variables de Entorno para Producción
Después de desplegar, configura en AWS Console:
- DJANGO_DEBUG=False
- DJANGO_ALLOWED_HOSTS=tu-app.elasticbeanstalk.com
- DJANGO_SECRET_KEY=tu-clave-secreta-generada
