from django.core.wsgi import get_wsgi_application

from render_bootstrap import bootstrap_django_settings


bootstrap_django_settings()
application = get_wsgi_application()
