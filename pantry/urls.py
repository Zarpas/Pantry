from django.urls import path
from . import views


urlpatterns = [
    path('', views.ubicacion_list, name='ubicacion_list')
]