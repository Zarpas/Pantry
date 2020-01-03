from django.urls import path
from . import views


urlpatterns = [
    path('', views.estado_general, name='estado_general'),
    path('ubicacion', views.ubicacion_list, name='ubicacion_list'),
]