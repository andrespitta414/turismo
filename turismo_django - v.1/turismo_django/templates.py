"""
TurismoDjango - HTML Templates
Todas las plantillas HTML definidas como strings en Python
para cumplir requisito de archivos .py
"""

# ===================== PLANTILLA BASE =====================

BASE_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Turismo Colombia{% endblock %}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f5f5f5; }
        
        /* Header */
        header { background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); color: white; padding: 1rem 0; }
        .header-content { max-width: 1200px; margin: 0 auto; padding: 0 20px; display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 1.8rem; font-weight: bold; }
        nav ul { list-style: none; display: flex; gap: 20px; }
        nav a { color: white; text-decoration: none; padding: 8px 15px; border-radius: 5px; transition: background 0.3s; }
        nav a:hover { background: rgba(255,255,255,0.2); }
        
        /* Container */
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        
        /* Cards */
        .card { background: white; border-radius: 10px; padding: 20px; margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .card h2 { color: #1e3c72; margin-bottom: 15px; border-bottom: 2px solid #1e3c72; padding-bottom: 10px; }
        
        /* Grid */
        .grid { display: grid; gap: 20px; }
        .grid-2 { grid-template-columns: repeat(2, 1fr); }
        .grid-3 { grid-template-columns: repeat(3, 1fr); }
        .grid-4 { grid-template-columns: repeat(4, 1fr); }
        
        /* Stats */
        .stat-card { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 10px; text-align: center; }
        .stat-card h3 { font-size: 2rem; }
        .stat-card p { opacity: 0.9; }
        
        /* Table */
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background: #1e3c72; color: white; }
        tr:hover { background: #f5f5f5; }
        
        /* Forms */
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; color: #333; font-weight: 500; }
        input, select { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px; font-size: 1rem; }
        input:focus, select:focus { outline: none; border-color: #1e3c72; }
        
        /* Buttons */
        .btn { padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-size: 1rem; text-decoration: none; display: inline-block; }
        .btn-primary { background: #1e3c72; color: white; }
        .btn-secondary { background: #6c757d; color: white; }
        .btn-danger { background: #dc3545; color: white; }
        .btn-success { background: #28a745; color: white; }
        .btn:hover { opacity: 0.9; }
        
        /* Messages */
        .messages { list-style: none; }
        .messages li { padding: 10px 15px; border-radius: 5px; margin-bottom: 10px; }
        .success { background: #d4edda; color: #155724; }
        .error { background: #f8d7da; color: #721c24; }
        .warning { background: #fff3cd; color: #856404; }
        .info { background: #d1ecf1; color: #0c5460; }
        
        /* Carrusel */
        .carrusel { display: flex; gap: 20px; overflow-x: auto; padding: 20px 0; }
        .destino-card { min-width: 300px; background: white; border-radius: 15px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        .destino-card .tipo { display: inline-block; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem; }
        .premium { background: #ffd700; color: #333; }
        .estandar { background: #e0e0e0; color: #333; }
        
        /* Navigation buttons */
        .nav-buttons { display: flex; justify-content: center; gap: 10px; margin-top: 20px; }
        
        /* Footer */
        footer { background: #333; color: white; text-align: center; padding: 20px 0; margin-top: 40px; }
        footer a { color: white; }
        
        /* Pagination */
        .pagination { display: flex; justify-content: center; gap: 10px; margin-top: 20px; }
        .pagination a { padding: 10px 15px; background: #1e3c72; color: white; border-radius: 5px; text-decoration: none; }
        
        /* Responsive */
        @media (max-width: 768px) {
            .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; }
            .header-content { flex-direction: column; gap: 15px; }
        }
    </style>
</head>
<body>
    <header>
        <div class="header-content">
            <div class="logo">Turismo Colombia</div>
            <nav>
                <ul>
                    <li><a href="/">Inicio</a></li>
                    <li><a href="/clientes/">Clientes</a></li>
                    <li><a href="/paquetes/">Paquetes</a></li>
                    <li><a href="/reservas/">Reservas</a></li>
                    <li><a href="/destinos/">Destinos</a></li>
                    <li><a href="/nosotros/">Nosotros</a></li>
                </ul>
            </nav>
        </div>
    </header>
    
    <main class="container">
        {% if messages %}
        <ul class="messages">
            {% for message in messages %}
            <li class="{{ message.tags }}">{{ message }}</li>
            {% endfor %}
        </ul>
        {% endif %}
        
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2026 Turismo Colombia - Sistema de Gestión de Turismo</p>
        <p>Desarrollado con Django | <a href="/datos-prueba/">Crear Datos de Prueba</a></p>
    </footer>
</body>
</html>
"""


# ===================== PLANTILLA INDEX =====================

INDEX_HTML = """
{% extends "base.html" %}

{% block title %}Inicio - Turismo Colombia{% endblock %}

{% block content %}
<!-- Dashboard Stats -->
<div class="grid grid-3" style="margin-bottom: 30px;">
    <div class="stat-card">
        <h3>{{ total_clientes }}</h3>
        <p>Clientes Registrados</p>
    </div>
    <div class="stat-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
        <h3>{{ total_paquetes }}</h3>
        <p>Paquetes Turísticos</p>
    </div>
    <div class="stat-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
        <h3>{{ total_reservas }}</h3>
        <p>Reservas Activas</p>
    </div>
</div>

<!-- Carrusel de Destinos (Lista Circular) -->
<div class="card">
    <h2>🌴 Destinos Destacados - Lista Circular</h2>
    <p>Explora nuestros destinos más populares. Usa los botones para navegar circularmente.</p>
    
    <form method="post" style="margin-top: 20px;">
        {% csrf_token %}
        <div class="carrusel">
            {% for destino in destinos_circular %}
            <div class="destino-card">
                <h3>{{ destino.destino }}</h3>
                <span class="tipo {{ destino.tipo_paquete|lower }}">{{ destino.tipo_paquete }}</span>
                <p style="margin-top: 10px;">📍 Guía: {{ destino.guia }}</p>
            </div>
            {% empty %}
            <p>No hay destinos disponibles. <a href="/datos-prueba/">Crear datos de prueba</a></p>
            {% endfor %}
        </div>
        <div class="nav-buttons">
            <button type="submit" name="accion" value="prev" class="btn btn-secondary">◀ Anterior</button>
            <button type="submit" name="accion" value="next" class="btn btn-primary">Siguiente ▶</button>
        </div>
    </form>
</div>

<!-- Recent Reservas -->
<div class="grid grid-2">
    <div class="card">
        <h2>📋 Últimas Reservas</h2>
        <table>
            <thead>
                <tr>
                    <th>Número</th>
                    <th>Cliente</th>
                    <th>Fecha</th>
                </tr>
            </thead>
            <tbody>
                {% for reserva in reservas_recientes %}
                <tr>
                    <td>{{ reserva.numero_reserva }}</td>
                    <td>{{ reserva.cliente.nombre }}</td>
                    <td>{{ reserva.fecha|date:"d/m/Y" }}</td>
                </tr>
                {% empty %}
                <tr><td colspan="3">No hay reservas</td></tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
    
    <div class="card">
        <h2>🏖️ Destinos Disponibles</h2>
        <table>
            <thead>
                <tr>
                    <th>Destino</th>
                    <th>Tipo</th>
                    <th>Guía</th>
                </tr>
            </thead>
            <tbody>
                {% for destino in destinos_circular %}
                <tr>
                    <td>{{ destino.destino }}</td>
                    <td><span class="tipo {{ destino.tipo_paquete|lower }}">{{ destino.tipo_paquete }}</span></td>
                    <td>{{ destino.guia }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>

<!-- Quick Actions -->
<div class="card">
    <h2>⚡ Acciones Rápidas</h2>
    <div style="display: flex; gap: 15px; flex-wrap: wrap;">
        <a href="/clientes/crear/" class="btn btn-primary">➕ Nuevo Cliente</a>
        <a href="/paquetes/crear/" class="btn btn-primary">➕ Nuevo Paquete</a>
        <a href="/reservas/crear/" class="btn btn-success">📅 Nueva Reserva</a>
        <a href="/destinos/" class="btn btn-secondary">🌴 Ver Destinos</a>
    </div>
</div>
{% endblock %}
"""


# ===================== PLANTILLA CLIENTE LIST =====================

CLIENTE_LIST_HTML = """
{% extends "base.html" %}

{% block title %}Clientes - Turismo Colombia{% endblock %}

{% block content %}
<div class="card">
    <h2>👥 Clientes</h2>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
        <form method="get" style="display: flex; gap: 10px;">
            <input type="text" name="buscar" placeholder="Buscar por nombre o cédula..." style="width: 300px;">
            <button type="submit" class="btn btn-primary">Buscar</button>
        </form>
        <a href="/clientes/crear/" class="btn btn-success">➕ Nuevo Cliente</a>
    </div>
    
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Cédula</th>
                <th>Correo</th>
                <th>Teléfono</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
            {% for cliente in clientes %}
            <tr>
                <td>{{ cliente.id }}</td>
                <td>{{ cliente.nombre }}</td>
                <td>{{ cliente.cedula }}</td>
                <td>{{ cliente.correo }}</td>
                <td>{{ cliente.numero }}</td>
                <td>
                    <a href="/clientes/{{ cliente.id }}/editar/" class="btn btn-secondary">Editar</a>
                    <a href="/clientes/{{ cliente.id }}/eliminar/" class="btn btn-danger">Eliminar</a>
                </td>
            </tr>
            {% empty %}
            <tr><td colspan="6">No hay clientes. <a href="/datos-prueba/">Crear datos de prueba</a></td></tr>
            {% endfor %}
        </tbody>
    </table>
    
    {% if clientes.has_other_page %}
    <div class="pagination">
        {% if clientes.has_previous %}
        <a href="?page={{ clientes.previous_page_number }}">Anterior</a>
        {% endif %}
        <span>Página {{ clientes.number }} de {{ clientes.paginator.num_pages }}</span>
        {% if clientes.has_next %}
        <a href="?page={{ clientes.next_page_number }}">Siguiente</a>
        {% endif %}
    </div>
    {% endif %}
</div>
{% endblock %}
"""


# ===================== PLANTILLA CLIENTE FORM =====================

CLIENTE_FORM_HTML = """
{% extends "base.html" %}

{% block title %}{{ accion }} Cliente - Turismo Colombia{% endblock %}

{% block content %}
<div class="card">
    <h2>👤 {{ accion }} Cliente</h2>
    <form method="post">
        {% csrf_token %}
        <div class="form-group">
            <label for="nombre">Nombre Completo:</label>
            <input type="text" id="nombre" name="nombre" value="{{ cliente.nombre|default:'' }}" required>
        </div>
        <div class="form-group">
            <label for="cedula">Cédula:</label>
            <input type="text" id="cedula" name="cedula" value="{{ cliente.cedula|default:'' }}" required>
        </div>
        <div class="form-group">
            <label for="correo">Correo Electrónico:</label>
            <input type="email" id="correo" name="correo" value="{{ cliente.correo|default:'' }}" required>
        </div>
        <div class="form-group">
            <label for="numero">Número de Teléfono:</label>
            <input type="text" id="numero" name="numero" value="{{ cliente.numero|default:'' }}" required>
        </div>
        <div style="display: flex; gap: 10px;">
            <button type="submit" class="btn btn-primary">Guardar</button>
            <a href="/clientes/" class="btn btn-secondary">Cancelar</a>
        </div>
    </form>
</div>
{% endblock %}
"""


# ===================== PLANTILLA CLIENTE DELETE =====================

CLIENTE_DELETE_HTML = """
{% extends "base.html" %}

{% block title %}Eliminar Cliente{% endblock %}

{% block content %}
<div class="card">
    <h2>🗑️ Eliminar Cliente</h2>
    <p>¿Está seguro de eliminar al cliente <strong>{{ cliente.nombre }}</strong>?</p>
    <p><strong>Cédula:</strong> {{ cliente.cedula }}</p>
    <form method="post">
        {% csrf_token %}
        <div style="display: flex; gap: 10px; margin-top: 20px;">
            <button type="submit" class="btn btn-danger">Eliminar</button>
            <a href="/clientes/" class="btn btn-secondary">Cancelar</a>
        </div>
    </form>
</div>
{% endblock %}
"""


# ===================== PLANTILLA PAQUETE LIST =====================

PAQUETE_LIST_HTML = """
{% extends "base.html" %}

{% block title %}Paquetes - Turismo Colombia{% endblock %}

{% block content %}
<div class="card">
    <h2>📦 Paquetes Turísticos</h2>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
        <form method="get" style="display: flex; gap: 10px;">
            <input type="text" name="buscar" placeholder="Buscar destino..." style="width: 250px;">
            <select name="tipo" style="width: 150px;">
                <option value="">Todos los tipos</option>
                <option value="Premium">Premium</option>
                <option value="Estandar">Estándar</option>
            </select>
            <button type="submit" class="btn btn-primary">Buscar</button>
        </form>
        <a href="/paquetes/crear/" class="btn btn-success">➕ Nuevo Paquete</a>
    </div>
    
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Tipo</th>
                <th>Destino</th>
                <th>Guía Asignado</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
            {% for paquete in paquetes %}
            <tr>
                <td>{{ paquete.id }}</td>
                <td><span class="tipo {{ paquete.tipo|lower }}">{{ paquete.tipo }}</span></td>
                <td>{{ paquete.destino }}</td>
                <td>{{ paquete.guia_asignado }}</td>
                <td>
                    <a href="/paquetes/{{ paquete.id }}/editar/" class="btn btn-secondary">Editar</a>
                    <a href="/paquetes/{{ paquete.id }}/eliminar/" class="btn btn-danger">Eliminar</a>
                </td>
            </tr>
            {% empty %}
            <tr><td colspan="5">No hay paquetes. <a href="/datos-prueba/">Crear datos de prueba</a></td></tr>
            {% endfor %}
        </tbody>
    </table>
</div>
{% endblock %}
"""


# ===================== PLANTILLA PAQUETE FORM =====================

PAQUETE_FORM_HTML = """
{% extends "base.html" %}

{% block title %}{{ accion }} Paquete{% endblock %}

{% block content %}
<div class="card">
    <h2>📦 {{ accion }} Paquete</h2>
    <form method="post">
        {% csrf_token %}
        <div class="form-group">
            <label for="tipo">Tipo de Paquete:</label>
            <select id="tipo" name="tipo" required>
                <option value="Estandar" {% if paquete.tipo == 'Estandar' %}selected{% endif %}>Estándar</option>
                <option value="Premium" {% if paquete.tipo == 'Premium' %}selected{% endif %}>Premium</option>
            </select>
        </div>
        <div class="form-group">
            <label for="destino">Destino:</label>
            <input type="text" id="destino" name="destino" value="{{ paquete.destino|default:'' }}" required>
        </div>
        <div class="form-group">
            <label for="guia_asignado">Guía Asignado:</label>
            <input type="text" id="guia_asignado" name="guia_asignado" value="{{ paquete.guia_asignado|default:'' }}" required>
        </div>
        <div style="display: flex; gap: 10px;">
            <button type="submit" class="btn btn-primary">Guardar</button>
            <a href="/paquetes/" class="btn btn-secondary">Cancelar</a>
        </div>
    </form>
</div>
{% endblock %}
"""


# ===================== PLANTILLA RESERVA LIST =====================

RESERVA_LIST_HTML = """
{% extends "base.html" %}

{% block title %}Reservas - Turismo Colombia{% endblock %}

{% block content %}
<div class="card">
    <h2>📅 Reservas</h2>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
        <form method="get" style="display: flex; gap: 10px;">
            <input type="text" name="buscar" placeholder="Buscar reserva o cliente..." style="width: 300px;">
            <button type="submit" class="btn btn-primary">Buscar</button>
        </form>
        <a href="/reservas/crear/" class="btn btn-success">➕ Nueva Reserva</a>
    </div>
    
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Número</th>
                <th>Fecha</th>
                <th>Cliente</th>
                <th>Paquete</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
            {% for reserva in reservas %}
            <tr>
                <td>{{ reserva.id }}</td>
                <td>{{ reserva.numero_reserva }}</td>
                <td>{{ reserva.fecha|date:"d/m/Y" }}</td>
                <td>{{ reserva.cliente.nombre }}</td>
                <td>{{ reserva.paquete.destino }} ({{ reserva.paquete.tipo }})</td>
                <td>
                    <a href="/reservas/{{ reserva.id }}/editar/" class="btn btn-secondary">Editar</a>
                    <a href="/reservas/{{ reserva.id }}/eliminar/" class="btn btn-danger">Eliminar</a>
                </td>
            </tr>
            {% empty %}
            <tr><td colspan="6">No hay reservas. <a href="/datos-prueba/">Crear datos de prueba</a></td></tr>
            {% endfor %}
        </tbody>
    </table>
</div>
{% endblock %}
"""


# ===================== PLANTILLA RESERVA FORM =====================

RESERVA_FORM_HTML = """
{% extends "base.html" %}

{% block title %}{{ accion }} Reserva{% endblock %}

{% block content %}
<div class="card">
    <h2>📅 {{ accion }} Reserva</h2>
    <form method="post">
        {% csrf_token %}
        <div class="form-group">
            <label for="numero_reserva">Número de Reserva:</label>
            <input type="text" id="numero_reserva" name="numero_reserva" value="{{ reserva.numero_reserva|default:'' }}" required placeholder="RES-XXX">
        </div>
        <div class="form-group">
            <label for="fecha">Fecha:</label>
            <input type="date" id="fecha" name="fecha" value="{{ reserva.fecha|date:'Y-m-d'|default:'' }}" required>
        </div>
        <div class="form-group">
            <label for="cliente">Cliente:</label>
            <select id="cliente" name="cliente" required>
                <option value="">Seleccionar cliente...</option>
                {% for c in clientes %}
                <option value="{{ c.id }}" {% if reserva.cliente.id == c.id %}selected{% endif %}>{{ c.nombre }} ({{ c.cedula }})</option>
                {% endfor %}
            </select>
        </div>
        <div class="form-group">
            <label for="paquete">Paquete:</label>
            <select id="paquete" name="paquete" required>
                <option value="">Seleccionar paquete...</option>
                {% for p in paquetes %}
                <option value="{{ p.id }}" {% if reserva.paquete.id == p.id %}selected{% endif %}>{{ p.destino }} - {{ p.tipo }}</option>
                {% endfor %}
            </select>
        </div>
        <div style="display: flex; gap: 10px;">
            <button type="submit" class="btn btn-primary">Guardar</button>
            <a href="/reservas/" class="btn btn-secondary">Cancelar</a>
        </div>
    </form>
</div>
{% endblock %}
"""


# ===================== PLANTILLA DESTINOS CIRCULAR =====================

DESTINOS_CIRCULAR_HTML = """
{% extends "base.html" %}

{% block title %}Destinos Destacados - Lista Circular{% endblock %}

{% block content %}
<div class="card">
    <h2>🌴 Destinos Destacados - Visualizador Circular</h2>
    <p>Esta sección usa una <strong>Lista Circular Manual</strong> para mostrar los destinos de forma infinita.</p>
    <p>La lógica de nodos permite navegar cíclicamente por los destinos.</p>
    
    <form method="post">
        {% csrf_token %}
        <div class="carrusel" style="margin: 30px 0;">
            {% for destino in destinos_circular %}
            <div class="destino-card" style="min-width: 350px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h3>{{ destino.destino }}</h3>
                    <span class="tipo {{ destino.tipo_paquete|lower }}">{{ destino.tipo_paquete }}</span>
                </div>
                <hr style="margin: 15px 0; opacity: 0.3;">
                <p>📍 <strong>Destino:</strong> {{ destino.destino }}</p>
                <p>👤 <strong>Guía:</strong> {{ destino.guia }}</p>
                <p>📦 <strong>Tipo:</strong> {{ destino.tipo_paquete }}</p>
            </div>
            {% empty %}
            <p>No hay destinos. Use el botón para crear datos de prueba.</p>
            {% endfor %}
        </div>
        
        <div class="nav-buttons">
            <button type="submit" name="accion" value="prev" class="btn btn-secondary">◀ Anterior (Nodo Anterior)</button>
            <span style="padding: 10px; background: #f0f0f0; border-radius: 5px;">Posición: {{ posicion_actual|add:1 }}</span>
            <button type="submit" name="accion" value="next" class="btn btn-primary">Siguiente (Próximo Nodo) ▶</button>
        </div>
    </form>
</div>

<div class="grid grid-2">
    <div class="card">
        <h2>🔄 Funcionamiento de la Lista Circular</h2>
        <ul style="line-height: 2;">
            <li>✅ <strong>Insertar:</strong> Agregar nuevos nodos al final</li>
            <li>✅ <strong>Eliminar:</strong> Quitar nodos por nombre de destino</li>
            <li>✅ <strong>Siguiente:</strong> Navegar al siguiente nodo</li>
            <li>✅ <strong>Anterior:</strong> Navegar al nodo anterior</li>
            <li>✅ <strong>Circularidad:</strong> Regresa al inicio al llegar al final</li>
        </ul>
    </div>
    <div class="card">
        <h2>📊 Datos de la Lista</h2>
        <p><strong>Total de destinos:</strong> {{ destinos_circular|length }}</p>
        <p><strong>Tipo de estructura:</strong> Lista Encadenada Circular</p>
        <p><strong>Uso:</strong> Visualización de destinos ocupados</p>
    </div>
</div>
{% endblock %}
"""


# ===================== PLANTILLA NOSOTROS =====================

NOSOTROS_HTML = """
{% extends "base.html" %}

{% block title %}Nosotros - Turismo Colombia{% endblock %}

{% block content %}
<div class="grid grid-2">
    <div class="card">
        <h2>🏢 Sobre Nosotros</h2>
        <p>Somos una empresa líder en tourismcolombiano, ofreciendo los mejores paquetes turísticos:</p>
        <ul style="margin: 20px; line-height: 2;">
            <li>🌴 Viajes a destinos paradisiacos</li>
            <li>👨‍🏫 Guías turísticos certificados</li>
            <li>⭐ Paquetes Premium y Estándar</li>
            <li>📅 Reservas flexibles</li>
        </ul>
    </div>
    <div class="card">
        <h2>🛠️ Tecnología</h2>
        <p>Este sistema está desarrollado con:</p>
        <ul style="margin: 20px; line-height: 2;">
            <li>🐍 Django Framework</li>
            <li>📊 Lista Circular Manual (Nodos)</li>
            <li>💾 Base de datos relacional</li>
            <li>🎨 UI/UX moderno</li>
        </ul>
    </div>
</div>

<div class="card">
    <h2>📞 Contacto</h2>
    <p><strong>Email:</strong>	info@turismocolombia.com</p>
    <p><strong>Teléfono:</strong> +57 310 123 4567</p>
    <p><strong>Dirección:</strong> Calle 123, Bogotá, Colombia</p>
</div>
{% endblock %}
"""


# ===================== DICCIONARIO DE PLANTILLAS =====================

TEMPLATES = {
    'base.html': BASE_TEMPLATE,
    'index.html': INDEX_HTML,
    'cliente_list.html': CLIENTE_LIST_HTML,
    'cliente_form.html': CLIENTE_FORM_HTML,
    'cliente_confirm_delete.html': CLIENTE_DELETE_HTML,
    'paquete_list.html': PAQUETE_LIST_HTML,
    'paquete_form.html': PAQUETE_FORM_HTML,
    'reserva_list.html': RESERVA_LIST_HTML,
    'reserva_form.html': RESERVA_FORM_HTML,
    'destinos_circular.html': DESTINOS_CIRCULAR_HTML,
    'nosotros.html': NOSOTROS_HTML,
}


def get_template(template_name):
    """Obtiene una plantilla por nombre"""
    return TEMPLATES.get(template_name, '')


# ===================== RENDERIZADOR DE PLANTILLAS (SIN DJANGO) =====================

def render_template(template_name, context=None):
    """
    Renderiza una plantilla manualmente (sin Django)
    Útil para testing o despliegue simple
    """
    from django.template import Template, Context
    from django.conf import settings
    
    if not settings.configured:
        from django.conf import settings as django_settings
        django_settings.configure(
            DEBUG=True,
            TEMPLATES=[{
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [],
                'APP_DIRS': True,
                'OPTIONS': {
                    'string_if_invalid': '{%s}}',
                },
            }],
        )
        import django
        django.setup()
    
    template_str = TEMPLATES.get(template_name, '')
    if not template_str:
        return f"Template {template_name} no encontrado"
    
    try:
        template = Template(template_str)
        ctx = Context(context or {})
        return template.render(ctx)
    except Exception as e:
        return f"Error al renderizar: {str(e)}"