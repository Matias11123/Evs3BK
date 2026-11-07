from django.core.management.base import BaseCommand
from canchas.models import Disciplina, Cancha

class Command(BaseCommand):
    help = 'Pobla la base de datos con disciplinas y canchas iniciales para el complejo deportivo.'

    def handle(self, *args, **kwargs):
        # Borra registros anteriores para evitar duplicados al volver a ejecutarlo
        Cancha.objects.all().delete()
        Disciplina.objects.all().delete()

        # 4 Clasificadores (Disciplinas requeridas por la pauta)
        d1 = Disciplina.objects.create(nombre="Pádel", descripcion="Deporte de raqueta en parejas con paredes de vidrio.")
        d2 = Disciplina.objects.create(nombre="Tenis", descripcion="Deporte tradicional en canchas de arcilla o superficie dura.")
        d3 = Disciplina.objects.create(nombre="Fútbolito", descripcion="Fútbol 7 en pasto sintético de alta calidad.")
        d4 = Disciplina.objects.create(nombre="Basketball", descripcion="Cancha techada de piso flotante profesional.")

        # 8 Entidades Principales (Canchas requeridas por la pauta)
        canchas_data = [
            (d1, "PAD-01", "Cancha Central Pádel", "Vidrio templado", 25000, 'DISPONIBLE'),
            (d1, "PAD-02", "Cancha Panorámica Pádel", "Cristal blindex", 28000, 'DISPONIBLE'),
            (d2, "TEN-01", "Cancha Arcilla 1", "Polvo de ladrillo", 20000, 'DISPONIBLE'),
            (d2, "TEN-02", "Cancha Dura 2", "Asfáltica profesional", 18000, 'MANTENCION'),
            (d3, "FUT-01", "Estadio Fútbolito A", "Pasto sintético FIFA", 45000, 'DISPONIBLE'),
            (d3, "FUT-02", "Estadio Fútbolito B", "Pasto sintético techado", 40000, 'DISPONIBLE'),
            (d4, "BAS-01", "Coliseo Central Básquet", "Piso flotante", 30000, 'DISPONIBLE'),
            (d4, "BAS-02", "Cancha Entrenamiento Básquet", "Sintético multigimnasio", 22000, 'DISPONIBLE'),
        ]

        for disc, cod, nom, sup, tarifa, est in canchas_data:
            Cancha.objects.create(
                disciplina=disc,
                codigo=cod,
                nombre=nom,
                superficie=sup,
                tarifa_bloque=tarifa,
                estado=est,
                activo=True
            )

        self.stdout.write(self.style.SUCCESS('¡Base de datos poblada exitosamente con 4 disciplinas y 8 canchas!'))