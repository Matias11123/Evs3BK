from django import forms
from .models import Cancha

class CanchaForm(forms.ModelForm):
    class Meta:
        model = Cancha
        fields = ['disciplina', 'codigo', 'nombre', 'superficie', 'tarifa_bloque', 'estado', 'imagen', 'activo']
        widgets = {
            'disciplina': forms.Select(attrs={'class': 'form-select'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: PAD-03'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la cancha'}),
            'superficie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Sintética, Vidrio templado'}),
            'tarifa_bloque': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    # Validación clean_() exigida en la pauta para valores cuantitativos no negativos
    def clean_tarifa_bloque(self):
        tarifa = self.cleaned_data.get('tarifa_bloque')
        if tarifa is not None and tarifa < 0:
            raise forms.ValidationError("La tarifa por bloque no puede ser un valor negativo.")
        return tarifa