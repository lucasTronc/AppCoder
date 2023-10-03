from django.urls import path
from .views import *
#importo funcionalidad de logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/',inicio, name="inicio"),
    path('contactTermPrivacy/',contactTermPrivacy, name="contactTermPrivacy"),
    path('formularioCliente/', formularioCliente, name="formularioCliente"),
    path('formularioProducto/', formularioProducto, name="formularioProducto"),
    path('formularioEnvio/', formularioEnvio, name="formularioEnvio"),
    path('mostrarformulario/', mostrarformulario, name="mostrarformulario"),
    path('buscar/', buscar, name="buscar"),
    path('about/', about, name="about"),
    path('listarProductos/', listarProductos, name="listarProductos"),
    path('login/', loginView, name="login"),
    path('register/', register, name="registro"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('editarPerfil/', editarPerfil, name="editarPerfil"),
]