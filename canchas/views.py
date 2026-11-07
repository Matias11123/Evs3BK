from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .models import Cancha, Disciplina
from .forms import CanchaForm

# R (Read) - Catálogo público con buscador Q, filtros y paginación
def catalogo_canchas(request):
    canchas_list = Cancha.objects.filter(activo=True).select_related('disciplina')
    disciplinas = Disciplina.objects.all()

    # Capturar parámetros de búsqueda y filtros
    busqueda = request.GET.get('q', '')
    disciplina_id = request.GET.get('disciplina', '')

    # Búsqueda simultánea multi-campo con objeto Q (Módulo 3.2)
    if busqueda:
        canchas_list = canchas_list.filter(
            Q(nombre__icontains=busqueda) |
            Q(codigo__icontains=busqueda) |
            Q(superficie__icontains=busqueda)
        )

    # Filtro por entidad de contexto (Disciplina)
    if disciplina_id:
        canchas_list = canchas_list.filter(disciplina_id=disciplina_id)

    # Paginación (4 canchas por página)
    paginator = Paginator(canchas_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'canchas/catalogo.html', {
        'page_obj': page_obj,
        'disciplinas': disciplinas,
        'busqueda': busqueda,
        'disciplina_seleccionada': disciplina_id
    })

# Ficha de detalle de la cancha
def detalle_cancha(request, pk):
    cancha = get_object_or_404(Cancha, pk=pk)
    return render(request, 'canchas/detalle_cancha.html', {'cancha': cancha})

# C (Create) - Creación con ModelForm y soporte multimedia (request.FILES)
def crear_cancha(request):
    if request.method == 'POST':
        form = CanchaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Cancha registrada exitosamente en el complejo!')
            return redirect('canchas:catalogo')
    else:
        form = CanchaForm()
    return render(request, 'canchas/cancha_form.html', {'form': form, 'titulo': 'Registrar Nueva Cancha'})

# U (Update) - Modificación con formulario precargado
def editar_cancha(request, pk):
    cancha = get_object_or_404(Cancha, pk=pk)
    if request.method == 'POST':
        form = CanchaForm(request.POST, request.FILES, instance=cancha)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Información de la cancha actualizada con éxito!')
            return redirect('canchas:catalogo')
    else:
        form = CanchaForm(instance=cancha)
    return render(request, 'canchas/cancha_form.html', {'form': form, 'titulo': 'Editar Cancha'})

# D (Delete) - Baja lógica segura con pantalla de confirmación
def eliminar_cancha(request, pk):
    cancha = get_object_or_404(Cancha, pk=pk)
    if request.method == 'POST':
        cancha.activo = False # Baja lógica solicitada en la pauta
        cancha.save()
        messages.warning(request, '¡La cancha ha sido dada de baja lógicamente del sistema!')
        return redirect('canchas:catalogo')
    return render(request, 'canchas/cancha_confirm_delete.html', {'cancha': cancha})