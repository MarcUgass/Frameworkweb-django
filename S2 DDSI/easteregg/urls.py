from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index2"),
    path("formulario2", views.procesarFormulario, name="formulario2"),
    path("genBD2", views.generarBaseDeDatos, name="genBD2"),
]