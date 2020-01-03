from django.shortcuts import render

# Create your views here.


def ubicacion_list(request):
    return render(request, 'pantry/ubicacion/list.html', {})
