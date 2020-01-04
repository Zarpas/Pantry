from django.urls import path
from . import views


urlpatterns = [
    path('', views.estado_general, name='estado_general'),

    # Urls dedicadas a la gestion de ubicaciones
    path('ubicacion', views.ubicacion_list, name='ubicacion_list'),
    path('ubicacion/<int:pk>/', views.ubicacion_detail, name='ubicacion_detail'),
    path('ubicacion/new/', views.ubicacion_new, name='ubicacion_new'),
    path('ubicacion/<int:pk>/edit/', views.ubicacion_edit, name='ubicacion_edit'),

    # Urls dedicadas a la gestion de estantes
    path('estante', views.estante_list, name='estante_list'),
    path('estante/<int:pk>/', views.estante_detail, name='estante_detail'),
    path('estante/new/', views.estante_new, name='estante_new'),
    path('estante/<int:pk>/edit/', views.estante_edit, name='estante_edit'),

    # Urls dedicadas a la gestion de referencias
    path('referencia', views.referencia_list, name='referencia_list'),
    path('referencia/<int:pk>/', views.referencia_detail, name='referencia_detail'),
    path('referencia/new/', views.referencia_new, name='referencia_new'),
    path('referencia/<int:pk>/edit/', views.referencia_edit, name='referencia_edit'),

    # Urls dedicada a la gestion de alimentos
    path('alimento', views.alimento_list, name='alimento_list'),
    path('alimento/<int:pk>/', views.alimento_detail, name='alimento_detail'),
    path('alimento/new/', views.alimento_new, name='alimento_new'),
    path('alimento/<int:pk>/edit/', views.alimento_edit, name='alimento_edit'),
]