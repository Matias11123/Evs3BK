from django.db import models
from django.core.validators import MinValueValidator

class Disciplina(models.Model):
    # Entidad de Contexto / Agrupación (Ej: Pádel, Tenis, Fútbol)
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre Disciplina")
    descripcion = models.TextField(verbose_name="Descripción")
    
    def __str__(self):
        return self.nombre

class Cancha(models.Model):
    # Entidad Principal Gestionable
    ESTADO_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('MANTENCION', 'En Mantención'),
        ('RESERVADA', 'Reservada'),
    ]
    
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, verbose_name="Disciplina")
    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código Único / Slug")
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Cancha")
    superficie = models.CharField(max_length=50, verbose_name="Tipo de Superficie (Sintética, Arcilla, etc.)")
    tarifa_bloque = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)], 
        verbose_name="Tarifa por Bloque Horario ($)"
    )
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='DISPONIBLE', verbose_name="Estado Operativo")
    imagen = models.ImageField(upload_to='canchas/', blank=True, null=True, verbose_name="Fotografía")
    activo = models.BooleanField(default=True, verbose_name="Baja Lógica (Activo)")

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"