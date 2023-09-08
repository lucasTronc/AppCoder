from django.urls import path
from .views import *

urlpatterns = [
   
    path('formularioCliente/', formularioCliente),
    path('formularioProducto/', formularioProducto),
    path('formularioEnvio/', formularioEnvio),
    path('mostrarformulario/', mostrarformulario),
]