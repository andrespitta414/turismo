from django.contrib import admin
from django.urls import path
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
import os

def health_check(request):
    """Health check endpoint"""
    return JsonResponse({
        'status': 'ok',
        'django': 'running',
        'debug': os.environ.get('DJANGO_DEBUG', 'False')
    })

def diagnostic_page(request):
    """Comprehensive diagnostic page"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Django Turismo - Diagnóstico</title>
        <style>
            body { font-family: Arial; padding: 2rem; max-width: 800px; margin: 0 auto; background: #f5f5f5; }
            h1 { color: #333; border-bottom: 2px solid #0066cc; padding-bottom: 10px; }
            h2 { color: #0066cc; margin-top: 2rem; }
            .status { padding: 1rem; margin: 1rem 0; border-radius: 5px; }
            .ok { background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
            .info { background: #d1ecf1; color: #0c5460; border: 1px solid #bee5eb; }
            code { background: #f4f4f4; padding: 2px 6px; border-radius: 3px; font-family: monospace; }
            .links { margin-top: 2rem; }
            .link-btn { display: inline-block; margin: 5px; padding: 10px 15px; background: #0066cc; color: white; text-decoration: none; border-radius: 5px; }
            .link-btn:hover { background: #0052a3; }
            table { width: 100%; border-collapse: collapse; margin: 1rem 0; }
            th, td { padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }
            th { background: #f9f9f9; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>🚀 Django Turismo - Diagnóstico</h1>
        
        <div class="status ok">
            <strong>✅ Django está corriendo correctamente</strong>
        </div>
        
        <h2>URLs Configuradas</h2>
        <table>
            <tr>
                <th>Ruta</th>
                <th>Descripción</th>
                <th>Enlace</th>
            </tr>
            <tr>
                <td><code>/</code></td>
                <td>Esta página de diagnóstico</td>
                <td><a href="/">Ir</a></td>
            </tr>
            <tr>
                <td><code>/health/</code></td>
                <td>Health check (JSON)</td>
                <td><a href="/health/">Ir</a></td>
            </tr>
            <tr>
                <td><code>/admin/</code></td>
                <td>Panel de administración Django</td>
                <td><a href="/admin/">Ir</a></td>
            </tr>
        </table>
        
        <h2>Información del Sistema</h2>
        <div class="status info">
            <strong>Debug Mode:</strong> """ + str(os.environ.get('DJANGO_DEBUG', 'False')) + """<br/>
            <strong>Allowed Hosts:</strong> """ + str(os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost')) + """<br/>
            <strong>Time Zone:</strong> """ + os.environ.get('TZ', 'America/Bogota') + """<br/>
            <strong>Language:</strong> es-es
        </div>
        
        <h2>Acciones</h2>
        <div class="links">
            <a href="/admin/" class="link-btn">📋 Admin Panel</a>
            <a href="/health/" class="link-btn">❤️ Health Check</a>
        </div>
        
        <h2>Instrucciones</h2>
        <div class="status info">
            <strong>Si ves esta página, tu Django está funcionando correctamente.</strong><br><br>
            <strong>Próximos pasos:</strong><br>
            1. Accede a <code>/admin/</code> para ver el panel de administración<br>
            2. Crea tu primera app con <code>python render_manage.py startapp miapp</code><br>
            3. Define tus modelos y vistas<br>
            4. Haz git push para que Render redepliegue automáticamente
        </div>
        
        <hr style="margin: 2rem 0; border: none; border-top: 1px solid #ddd;">
        <p style="color: #666; font-size: 14px; text-align: center;">
            Django Turismo en Render.com ✨
        </p>
    </body>
    </html>
    """
    return HttpResponse(html, content_type='text/html; charset=utf-8')

urlpatterns = [
    path('', diagnostic_page, name='home'),  # Página de diagnóstico en raíz
    path('health/', health_check, name='health'),
    path('admin/', admin.site.urls),
]
