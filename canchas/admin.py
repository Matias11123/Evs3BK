from django.contrib import admin
from .models import Disciplina, Cancha

# 1. Personalización de los encabezados globales del Admin (Módulo 2.1)
admin.site.site_header = 'Complejo Deportivo Gol Master Chillán - Panel de Control'
admin.site.site_title = 'Gol Master Admin'
admin.site.index_title = 'Gestión Operativa de Recursos y Servicios'

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Cancha)
class CanchaAdmin(admin.ModelAdmin):
    # 2. Configuración Avanzada de ModelAdmin (Módulo 2.2)
    list_display = ('codigo', 'nombre', 'disciplina', 'tarifa_bloque', 'estado', 'activo')
    list_filter = ('disciplina', 'estado', 'activo')
    search_fields = ('codigo', 'nombre', 'superficie')
    list_editable = ('tarifa_bloque', 'estado', 'activo') # Edición rápida en grilla
    
    # Estructura modular del formulario en secciones lógicas
    fieldsets = (
        ('Información Principal', {
            'fields': ('disciplina', 'codigo', 'nombre')
        }),
        ('Detalles Técnicos y Tarifarios', {
            'fields': ('superficie', 'tarifa_bloque')
        }),
        ('Control Operativo y Multimedia', {
            'fields': ('estado', 'activo', 'imagen')
        }),
    )