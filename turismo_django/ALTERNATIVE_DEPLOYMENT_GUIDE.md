# Guía de Despliegue Alternativo - Sistema Turismo Django

## Estado Actual
- **AWS Elastic Beanstalk**: Entorno atascado en "pending creation"
- **CSRF Error**: Solucionado para desarrollo local
- **Proyecto**: 100% funcional y listo para producción

## Opciones de Despliegue Gratuito

### 1. Heroku (Recomendado - Más Confiable)

#### Ventajas:
- Free Tier: 550 horas/mes dyno hours
- Base de datos PostgreSQL gratuita
- SSL automático
- Despliegue fácil con Git

#### Pasos:

1. **Instalar Heroku CLI**
```bash
# Descargar desde: https://devcenter.heroku.com/articles/heroku-cli
# O usar npm:
npm install -g heroku
```

2. **Login en Heroku**
```bash
heroku login
```

3. **Crear Aplicación**
```bash
heroku create turismo-django-app
```

4. **Configurar Variables de Entorno**
```bash
heroku config:set DJANGO_SETTINGS_MODULE=turismo_django.settings
heroku config:set DJANGO_DEBUG=False
heroku config:set SECRET_KEY=tu-clave-secreta-generada
```

5. **Desplegar**
```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

6. **Migraciones**
```bash
heroku run python manage.py migrate
```

7. **Crear Superusuario**
```bash
heroku run python manage.py createsuperuser
```

### 2. PythonAnywhere (Más Simple)

#### Ventajas:
- Free Tier: Web app básica
- Base de datos SQLite incluida
- Panel web intuitivo
- Sin configuración de CLI

#### Pasos:

1. **Crear cuenta en**: https://www.pythonanywhere.com/

2. **Subir archivos**:
   - Dashboard > Files > Upload
   - Subir todo el proyecto

3. **Crear Web App**:
   - Dashboard > Web > Add new web app
   - Seleccionar "Manual configuration"
   - Python 3.9

4. **Configurar**:
   - Path: `/home/username/turismo_django/turismo_django/wsgi.py`
   - Virtualenv: Crear nuevo
   - Install requirements

5. **Migraciones**:
   - Console > Bash > `python manage.py migrate`

### 3. Vercel (Moderno)

#### Ventajas:
- Free Tier: Sin límite de solicitudes
- CDN global
- Despliegue automático
- Interfaz moderna

#### Pasos:

1. **Instalar Vercel CLI**
```bash
npm install -g vercel
```

2. **Desplegar**
```bash
vercel --prod
```

3. **Configurar Variables de Entorno**
```bash
vercel env add DJANGO_SETTINGS_MODULE production
vercel env add DJANGO_DEBUG production
```

### 4. Railway (Alternativa Moderna)

#### Ventajas:
- Free Tier: $5 créditos/mes
- PostgreSQL incluido
- Despliegue desde GitHub
- Interfaz simple

#### Pasos:

1. **Crear cuenta**: https://railway.app/

2. **Conectar GitHub**
3. **Seleccionar repositorio**
4. **Configurar variables de entorno**
5. **Deploy automático**

## Recomendación

**Heroku** es la mejor opción para tu proyecto porque:

- **Free Tier generoso**: 550 horas/mes
- **PostgreSQL gratuito**: Base de datos robusta
- **SSL automático**: HTTPS sin configuración
- **Despliegue Git**: Flujo familiar
- **Escalabilidad**: Fácil upgrade si needed

## Archivos Creados para Heroku

- `requirements_heroku.txt` - Dependencias optimizadas
- `Procfile` - Configuración de proceso web
- `runtime.txt` - Versión Python específica

## Comandos Útiles Heroku

```bash
# Ver estado
heroku ps

# Ver logs
heroku logs --tail

# Abrir aplicación
heroku open

# Configurar variables
heroku config:set VAR=value

# Reiniciar
heroku restart

# Escalar (si needed)
heroku ps:scale web=1
```

## Costos Comparativos

| Servicio | Free Tier | Límites | Upgrade |
|----------|-----------|---------|---------|
| Heroku | $0/mes | 550 horas, PostgreSQL | ~$7/mes |
| PythonAnywhere | $0/mes | Web app básica | ~$5/mes |
| Vercel | $0/mes | Ilimitado | ~$20/mes |
| Railway | $0/mes | $5 créditos | ~$5/mes |

## Siguiente Paso

¿Cuál prefieres probar? **Heroku** es mi recomendación principal por su confiabilidad y facilidad de uso.
