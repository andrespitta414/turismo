# Deploy en Render.com (Django)

Guia corta y directa para desplegar este proyecto en Render.

## 1) Configuracion en Render

En Render crea un **Web Service** desde tu repo de GitHub.

- Environment: `Python 3`
- Build Command:
  ```bash
  pip install -r requirements.txt && python render_manage.py collectstatic --noinput && python render_manage.py migrate --noinput
  ```
- Start Command:
  ```bash
  gunicorn wsgi_render:application --bind 0.0.0.0:$PORT
  ```

## 2) Variables de entorno

En el servicio agrega:

```bash
DJANGO_SECRET_KEY=pon_una_clave_larga_y_segura
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=tu-servicio.onrender.com
DJANGO_CSRF_TRUSTED_ORIGINS=https://tu-servicio.onrender.com
DJANGO_SECURE_SSL_REDIRECT=True
DJANGO_SESSION_COOKIE_SECURE=True
DJANGO_CSRF_COOKIE_SECURE=True
```

Para base de datos en Render PostgreSQL, agrega ademas:

```bash
DATABASE_URL=postgres://...
```

## 3) Nota importante de datos

Si no defines `DATABASE_URL`, la app usa SQLite y en Render eso es efimero (puedes perder datos al redeploy/restart).

Para persistencia real:
- usa PostgreSQL de Render, o
- monta un Disk persistente y ajusta la ruta de SQLite.

## 4) Verificacion post-deploy

En Render Logs valida que no haya errores de `migrate` ni `gunicorn`.

Prueba estas rutas:
- `/`
- `/admin`

Si aparece `DisallowedHost`, corrige `DJANGO_ALLOWED_HOSTS` con el dominio exacto de Render.

## 5) Comandos locales utiles

```bash
python manage.py check
python manage.py migrate
python manage.py runserver
```
