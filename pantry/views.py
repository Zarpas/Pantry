from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Ubicacion, Estante, Referencia, Alimento
from .forms import UbicacionForm, EstanteForm, ReferenciaForm, AlimentoForm

# Create your views here.


def estado_general(request):
    return render(request, 'pantry/estado/list.html', {})


def ubicacion_list(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'pantry/ubicacion/list.html', {'ubicaciones': ubicaciones})


def estante_list(request):
    estantes = Estante.objects.all()
    return render(request, 'pantry/estante/list.html', {'estantes': estantes})


def referencia_list(request):
    referencias = Referencia.objects.all()
    return render(request, 'pantry/referencia/list.html', {'referencias': referencias})


def alimento_list(request):
    alimentos = Alimento.objects.all()
    return render(request, 'pantry/alimento/list.html', {'alimentos': alimentos})


def ubicacion_detail(request, pk):
    ubicacion = get_object_or_404(Ubicacion, pk=pk)
    return render(request, 'pantry/ubicacion/detail.html', {'ubicacion': ubicacion})


def estante_detail(request, pk):
    estante = get_object_or_404(Estante, pk=pk)
    return render(request, 'pantry/estante/detail.html', {'estante': estante})


def referencia_detail(request, pk):
    referencia = get_object_or_404(Referencia, pk=pk)
    return render(request, 'pantry/referencia/detail.html', {'referencia': referencia})


def alimento_detail(request, pk):
    alimento = get_object_or_404(Alimento, pk=pk)
    return render(request, 'pantry/alimento/detail.html', {'alimento': alimento})


def ubicacion_new(request):
    if request.method == "POST":
        form = UbicacionForm(request.POST)
        if form.is_valid():
            ubicacion = form.save(commit=False)
            ubicacion.save()
            return redirect('ubicacion_detail', pk=ubicacion.pk)
    else:
        form = UbicacionForm()
    return render(request, 'pantry/ubicacion/new.html', {'form': form})


def estante_new(request):
    if request.method == "POST":
        form = EstanteForm(request.POST)
        if form.is_valid():
            estante = form.save(commit=False)
            estante.save()
            return redirect('estante_detail', pk=estante.pk)
    else:
        form = EstanteForm()
    return render(request, 'pantry/estante/new.html', {'form': form})


def referencia_new(request):
    if request.method == "POST":
        form = ReferenciaForm(request.POST)
        if form.is_valid():
            referencia = form.save(commit=False)
            referencia.save()
            return redirect('referencia_detail', pk=referencia.pk)
    else:
        form = ReferenciaForm()
    return render(request, 'pantry/referencia/new.html', {'form': form})


def alimento_new(request):
    if request.method == "POST":
        form = AlimentoForm(request.POST)
        if form.is_valid():
            alimento = form.save(commit=False)
            alimento.save()
            return redirect('alimento_detail', pk=alimento.pk)
    else:
        form = AlimentoForm()
    return render(request, 'pantry/alimento/new.html', {'form': form})


def ubicacion_edit(request, pk):
    ubicacion = get_object_or_404(Ubicacion, pk=pk)
    if request.method == "POST":
        form = UbicacionForm(request.POST, instance=ubicacion)
        if form.is_valid():
            ubicacion = form.save(commit=False)
            ubicacion.save()
            return redirect('ubicacion_detail', pk=ubicacion.pk)
    else:
        form = UbicacionForm(instance=ubicacion)
    return render(request, 'pantry/ubicacion/new.html', {'form': form})


def estante_edit(request, pk):
    estante = get_object_or_404(Estante, pk=pk)
    if request.method == "POST":
        form = EstanteForm(request.POST, instance=estante)
        if form.is_valid():
            estante = form.save(commit=False)
            estante.save()
            return redirect('estante_detail', pk=estante.pk)
    else:
        form = EstanteForm(instance=estante)
    return render(request, 'pantry/estante/new.html', {'form': form})


def referencia_edit(request, pk):
    referencia = get_object_or_404(Referencia, pk=pk)
    if request.method == "POST":
        form = ReferenciaForm(request.POST, instance=referencia)
        if form.is_valid():
            referencia = form.save(commit=False)
            referencia.save()
            return redirect('referencia_detail', pk=referencia.pk)
    else:
        form = ReferenciaForm(instance=referencia)
    return render(request, 'pantry/referencia/new.html', {'form': form})


def alimento_edit(request, pk):
    alimento = get_object_or_404(Alimento, pk=pk)
    if request.method == "POST":
        form = AlimentoForm(request.POST, instance=alimento)
        if form.is_valid():
            alimento = form.save(commit=False)
            alimento.save()
            return redirect('alimento_detail', pk=alimento_pk)
    else:
        form = AlimentoForm(instance=alimento)
    return render(request, 'pantry/alimento/new.html', {'form': form})
