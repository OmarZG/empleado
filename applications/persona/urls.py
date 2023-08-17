from django.contrib import admin
from django.urls import path

from . import views

app_name = 'persona_app'

urlpatterns = [
    path(
        '',
        views.InicioView.as_view(),
        name='inicio'
    ),
    path('listar-todo-empleados/',
        views.ListAllEmpleados.as_view(),
        name='empleados_all'
        ),
    path(
        'listar-by-area/<shorname>/',
        views.ListByAreaEmpleado.as_view(),
        name='empleados_area'
    ),
    path(
        'lista-empleados-admin/',
        views.ListaEmpleadosAdmin.as_view(),
        name='empleados_admin'
    ),
    path('buscar-empleado/',
        views.ListEmpleadosByKword.as_view(),
        name='buscar_empleado'
        ),
    path(
        'listar-habilidades-empleado/<id>/',
        views.ListHabilidadesEmpleado.as_view(),
        name='habilidades_empleados'
    ),
    path('ver-empleado/<pk>/',
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'
        ),
    path('add-empleado/',
        views.EmpleadoCreateView.as_view(),
        name='empleado_add'
        ),
    path(
        'success/',
        views.SucessView.as_view(),
        name='correcto'
    ),
    path(
        'update-empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
    ),
    path(
        'delete-empleado/<pk>/',
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado'
    ),
]
