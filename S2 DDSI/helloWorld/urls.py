from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("formulario", views.procesarFormulario, name="formulario"),
    path("genBD", views.generarBaseDeDatos, name="genBD"),
]