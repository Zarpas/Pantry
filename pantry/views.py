from django.shortcuts import render
from django.utils import timezone
from .models import Ubicacion

# Create your views here.


def estado_general(request):
    return render(request, 'pantry/estado/list.html', {})


def ubicacion_list(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'pantry/ubicacion/list.html', {'ubicaciones': ubicaciones})
