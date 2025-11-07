from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.inicio_in_n_out, name='inicio'),

    # ============= Sucursal ============
    path('sucursal/agregar/', views.agregar_sucursal, name='agregar_sucursal'),
    path('sucursal/ver/', views.ver_sucursales, name='ver_sucursales'),
    path('sucursal/actualizar/<int:sucursal_id>/', views.actualizar_sucursal, name='actualizar_sucursal'),
    path('sucursal/actualizar/realizar/<int:sucursal_id>/', views.realizar_actualizacion_sucursal, name='realizar_actualizacion_sucursal'),
    path('sucursal/borrar/<int:sucursal_id>/', views.borrar_sucursal, name='borrar_sucursal'),

    # ============= TRABAJADOR ============
    path('trabajador/agregar/', views.agregar_trabajador, name='agregar_trabajador'),
    path('trabajador/ver/', views.ver_trabajadores, name='ver_trabajadores'),
    path('trabajador/actualizar/<int:trabajador_id>/', views.actualizar_trabajador, name='actualizar_trabajador'),
    path('trabajador/actualizar/realizar/<int:trabajador_id>/', views.realizar_actualizacion_trabajador, name='realizar_actualizacion_trabajador'),
    path('trabajador/borrar/<int:trabajador_id>/', views.borrar_trabajador, name='borrar_trabajador'),
]