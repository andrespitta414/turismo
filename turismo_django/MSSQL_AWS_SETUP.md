# MSSQL en Django + AWS Elastic Beanstalk

Esta configuracion usa `mssql-django` con `pyodbc`, que es el backend oficial soportado por Microsoft para Django sobre SQL Server.

Fuentes usadas:
- [mssql-django en PyPI](https://pypi.org/project/mssql-django/)
- [Repositorio oficial microsoft/mssql-django](https://github.com/microsoft/mssql-django)
- [Instalar Microsoft ODBC Driver 18 para SQL Server en Linux](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver17)

## Dependencias del proyecto

Ya quedaron agregadas en `requirements.txt`:

- `mssql-django==1.7`
- `pyodbc==5.3.0`

## Variables de entorno para MSSQL

Si vas a usar SQL Server, define como minimo:

```bash
DB_ENGINE=mssql
DB_NAME=tu_base
DB_USER=tu_usuario
DB_PASSWORD=tu_password
DB_HOST=tu_servidor_o_ip
DB_PORT=1433
DB_DRIVER=ODBC Driver 18 for SQL Server
DB_EXTRA_PARAMS=Encrypt=yes;TrustServerCertificate=yes
DB_CONNECTION_TIMEOUT=30
DB_CONNECTION_RETRIES=5
DB_CONNECTION_RETRY_BACKOFF_TIME=5
DB_QUERY_TIMEOUT=30
DATABASE_CONNECTION_POOLING=True
```

## Comando sugerido en Elastic Beanstalk

```bash
eb setenv DJANGO_SECRET_KEY="pon_aqui_una_clave_larga_y_segura" DJANGO_DEBUG=False DJANGO_ALLOWED_HOSTS="tu-entorno.us-east-1.elasticbeanstalk.com,.elasticbeanstalk.com" DJANGO_CSRF_TRUSTED_ORIGINS="http://tu-entorno.us-east-1.elasticbeanstalk.com,https://tu-entorno.us-east-1.elasticbeanstalk.com" DJANGO_SECURE_SSL_REDIRECT=False DJANGO_SESSION_COOKIE_SECURE=False DJANGO_CSRF_COOKIE_SECURE=False DB_ENGINE=mssql DB_NAME="tu_base" DB_USER="tu_usuario" DB_PASSWORD="tu_password" DB_HOST="tu_servidor_o_ip" DB_PORT=1433 DB_DRIVER="ODBC Driver 18 for SQL Server" DB_EXTRA_PARAMS="Encrypt=yes;TrustServerCertificate=yes"
```

## Nota importante sobre AWS Elastic Beanstalk

Tu aplicacion ya sabe conectarse a MSSQL, pero para que funcione en Amazon Linux 2023 tambien necesitas tener instalado un driver ODBC compatible en la instancia.

La documentacion oficial de Microsoft soporta Linux con ODBC Driver 18, pero Amazon Linux no aparece listado explicitamente en la guia oficial. Por eso:

- la configuracion Django ya queda lista
- el siguiente paso operativo es instalar y validar el driver ODBC en el entorno AWS que vayas a usar

## Flujo recomendado

1. Levantar un nuevo entorno de pruebas en Elastic Beanstalk.
2. Instalar y verificar el driver ODBC 18 en la instancia.
3. Configurar las variables `DB_*`.
4. Ejecutar `eb deploy`.
5. Probar `python manage.py migrate` contra MSSQL.

## Verificacion rapida

Cuando tengas credenciales reales, estas pruebas son las correctas:

```bash
python manage.py check
python manage.py migrate
```

Si la conexion falla, normalmente sera por una de estas causas:

- ODBC Driver no instalado en la instancia
- puerto 1433 bloqueado por firewall o security group
- SQL Server no accesible publicamente desde AWS
- `Encrypt` o `TrustServerCertificate` mal configurados
- autenticacion SQL Server deshabilitada en el servidor
