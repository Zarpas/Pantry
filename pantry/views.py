from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Ubicacion

# Create your views here.


def estado_general(request):
    return render(request, 'pantry/estado/list.html', {})


def ubicacion_list(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'pantry/ubicacion/list.html', {'ubicaciones': ubicaciones})


def ubicacion_detail(request, pk):
    ubicacion = get_object_or_404(Ubicacion, pk=pk)
    return render(request, 'pantry/ubicacion/detail.html', {'ubicacion': ubicacion})
