# Despliegue en AWS Elastic Beanstalk

## Cambios preparados en el proyecto

- `settings.py` corregido para usar un `BASE_DIR` valido.
- Seguridad de produccion activada cuando `DJANGO_DEBUG=False`.
- WhiteNoise agregado para servir archivos estaticos.
- `collectstatic` y `migrate` configurados para ejecutarse en Elastic Beanstalk.

## Variables de entorno obligatorias

Define estas variables antes del primer despliegue:

```bash
DJANGO_SECRET_KEY=pon_aqui_una_clave_larga_y_segura
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=tu-entorno.us-east-1.elasticbeanstalk.com
DJANGO_CSRF_TRUSTED_ORIGINS=http://tu-entorno.us-east-1.elasticbeanstalk.com,https://tu-entorno.us-east-1.elasticbeanstalk.com
DJANGO_SECURE_SSL_REDIRECT=False
DJANGO_SESSION_COOKIE_SECURE=False
DJANGO_CSRF_COOKIE_SECURE=False
```

## Comandos sugeridos

Instala AWS CLI y EB CLI:

```bash
pip install awscli awsebcli
```

Configura tus credenciales:

```bash
aws configure
```

Inicializa Elastic Beanstalk desde la raiz del proyecto:

```bash
eb init -p python-3.9 turismo-django
```

Crea el entorno:

```bash
eb create production-env
```

Configura variables:

```bash
eb setenv DJANGO_SECRET_KEY="pon_aqui_una_clave_larga_y_segura" DJANGO_DEBUG=False DJANGO_ALLOWED_HOSTS="production-env.us-east-1.elasticbeanstalk.com,.elasticbeanstalk.com" DJANGO_CSRF_TRUSTED_ORIGINS="http://production-env.us-east-1.elasticbeanstalk.com,https://production-env.us-east-1.elasticbeanstalk.com" DJANGO_SECURE_SSL_REDIRECT=False DJANGO_SESSION_COOKIE_SECURE=False DJANGO_CSRF_COOKIE_SECURE=False
```

Despliega:

```bash
eb deploy
```

Revisa estado y logs:

```bash
eb status
eb logs
```

## Nota importante

El proyecto queda listo para desplegar en HTTP sobre Elastic Beanstalk. Cuando configures HTTPS con certificado en el Load Balancer, cambia estas variables a `True`:

```bash
DJANGO_SECURE_SSL_REDIRECT=True
DJANGO_SESSION_COOKIE_SECURE=True
DJANGO_CSRF_COOKIE_SECURE=True
```

Por ahora el proyecto queda listo para desplegar con SQLite o con PostgreSQL via variables RDS ya existentes. La conexion a MSSQL la dejamos en espera hasta que me compartas los datos del servidor y el driver objetivo.
