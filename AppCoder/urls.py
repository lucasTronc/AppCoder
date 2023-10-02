from django.urls import path
from .views import *

urlpatterns = [
    path('inicio/',inicio, name="inicio"),
    path('formularioCliente/', formularioCliente, name="formularioCliente"),
    path('formularioProducto/', formularioProducto, name="formularioProducto"),
    path('formularioEnvio/', formularioEnvio, name="formularioEnvio"),
    path('mostrarformulario/', mostrarformulario, name="mostrarformulario"),
    path('buscar/', buscar, name="buscar"),
    path('about/', about, name="about"),
    path('listarProductos/', listarProductos, name="listarProductos"),
    path('login/', loginView, name="login"),
    path('register/', register, name="registro"),
]