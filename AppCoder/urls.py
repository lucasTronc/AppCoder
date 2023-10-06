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
    path('login/', loginView, name="login"),
    path('register/', register, name="registro"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('editarPerfil/', editarPerfil, name="editarPerfil"),
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar"),
    path('listaClientes/', ListarClientes.as_view(), name="listarClientes"),
    path('detalleClientes/<pk>/', DetalleClientes.as_view(), name="detalleClientes"),
    path('listarProductos/', ListarProductos.as_view(), name="listarProductos"),
    path('detalleProductos/<pk>/', DetalleProductos.as_view(), name="detalleProductos"),
    path('listarEnvios/', ListarEnvios.as_view(), name="listarEnvios"),
    path('detalleEnvios/<pk>/', DetalleEnvios.as_view(), name="detalleEnvios"),
 
]