from django.urls import path
from .views import *

urlpatterns = [
   
    path('formularioCliente/', formularioCliente, name="formularioCliente"),
    path('formularioProducto/', formularioProducto, name="formularioProducto"),
    path('formularioEnvio/', formularioEnvio, name="formularioEnvio"),
    path('mostrarformulario/', mostrarformulario, name="mostrarformulario"),
]