# ⚽ Complejo Deportivo Gol Master Chillán - Sistema de Gestión y Reservas

Sistema web desarrollado como Evaluación Sumativa de desarrollo back-end utilizando el framework **Django**. La plataforma permite la gestión administrativa y comercial de canchas deportivas, control de disciplinas, operaciones CRUD completas con soporte multimedia, y un sistema transitorio de reservas basado en sesiones HTTP (`request.session`).

---

## 🚀 Ficha Técnica
* **Asignatura / Programa:** Analista Programador - INACAP Sede Chillán
* **Tecnología Back-End:** Python 3.10+, Django 6.1.3
* **Base de Datos:** SQLite (Desarrollo) / PostgreSQL compatible
* **Frontend & UI:** Bootstrap 5, Bootstrap Icons, HTML5 responsivo
* **Librerías de Apoyo:** `Pillow` (Gestión de imágenes), `python-dotenv` (Variables de entorno)

---

## 📂 Estructura del Proyecto
```text
Evs3BK/
├── canchas/                   # Aplicación principal del negocio
│   ├── migrations/            # Historial de migraciones de la BD
│   ├── templates/canchas/     # Vistas HTML (Catálogo, Detalle, Formularios, Carrito)
│   ├── admin.py               # Configuración avanzada del panel de control
│   ├── forms.py               # Formularios ModelForm y validaciones clean_()
│   ├── models.py              # Modelos relacionales (Disciplina y Cancha)
│   ├── views.py               # Vistas, lógica de negocio, paginación y sesiones
│   └── urls.py                # Enrutamiento de la aplicación
├── complejo_deportivo_project/ # Configuración global del proyecto
│   ├── settings.py            # Ajustes de entorno, apps, multimedia y BD
│   └── urls.py                # Enrutador raíz y soporte MEDIA_URL
├── templates/                 # Plantilla maestra global (base.html)
├── media/                     # Almacenamiento local de archivos multimedia
├── manage.py                  # Utilidad de línea de comandos de Django
├── requirements.txt           # Dependencias del proyecto
└── .env.example               # Plantilla de variables de entorno seguras

⚙️ Guía de Instalación y Ejecución Local
Sigue estos pasos para clonar y ejecutar el proyecto en tu entorno de desarrollo local:

Clonar el repositorio:

PowerShell
git clone <url-del-repositorio>
cd Evs3BK
Crear y activar el entorno virtual:

PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
Instalar dependencias:

PowerShell
pip install -r requirements.txt
Configurar variables de entorno:
Crea un archivo .env en la raíz del proyecto basado en el archivo .env.example y configura tu SECRET_KEY y DEBUG=True.

Aplicar migraciones y poblar datos iniciales:

PowerShell
python manage.py makemigrations
python manage.py migrate
python manage.py poblar_datos
Ejecutar el servidor de desarrollo:

PowerShell
python manage.py runserver
Accede a la web en http://127.0.0.1:8000/ y al panel de administración en http://127.0.0.1:8000/admin/.

🤖 Bitácora de Uso Técnico y Ético de Inteligencia Artificial
Como parte de los estándares de desarrollo moderno, se documenta el uso de asistencia de Inteligencia Artificial para la resolución de desafíos arquitectónicos, consultas de ORM y buenas prácticas de seguridad.

Prompt 1: Arquitectura de Modelos y Relación de Integridad (ForeignKey)
Prompt utilizado: "Necesito estructurar los modelos en Django ORM para un complejo deportivo con Disciplinas y Canchas. ¿Cómo debo configurar la relación ForeignKey para evitar borrados accidentales de disciplinas que tienen canchas asociadas, y cómo añado validaciones numéricas estrictas para evitar tarifas negativas?"

Justificación técnica y adaptación: La IA sugirió el uso de on_delete=models.PROTECT para proteger la integridad referencial a nivel de base de datos relacional. Asimismo, se adaptó el validador MinValueValidator y el método clean_tarifa_bloque() en el formulario para asegurar que la lógica de negocio rechace de inmediato montos menores a cero, cumpliendo con la robustez exigida en la pauta académica.

Prompt 2: Buscador Multi-campo Avanzado y Paginación con Q
Prompt utilizado: "¿Cómo implemento una vista en Django que permita buscar simultáneamente por texto en varios campos (nombre, código, superficie) usando el objeto Q, combinándolo con un filtro por categoría y paginación con Paginator?"

Justificación técnica y adaptación: Se adoptó la estructura del objeto Q combinada mediante operadores lógicos | (OR) para construir consultas SQL eficientes sin sobrecargar la aplicación. Se integró directamente con los parámetros GET del navegador y la paginación de 4 elementos por página para optimizar la experiencia de usuario en el catálogo público responsivo.

Prompt 3: Gestión de Carrito Transitorio con Sesiones HTTP (request.session)
Prompt utilizado: "Explícame cómo implementar un carrito de compras temporal basado puramente en sesiones de Django (request.session) para un sistema de reservas de canchas, permitiendo agregar ítems, calcular subtotales y vaciar la sesión."

Justificación técnica y adaptación: Permitió diseñar el flujo transitorio donde los datos del cliente no requieren persistencia inmediata en bases de datos relacionales pesadas hasta confirmar la transacción. Se adaptó la estructura de diccionarios dentro de la sesión con claves tipadas y control de marcas de modificación (request.session.modified = True) para garantizar la reactividad del estado web.