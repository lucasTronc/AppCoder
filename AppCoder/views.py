from django.shortcuts import render

# Create your views here.

def formularioCliente(req):
    return render(req,"formularioCliente.html")

def formularioProducto(req):
    return render(req,"formularioProducto.html")

def formularioEnvio(req):
    return render(req,"formularioEnvio.html")

def mostrarformulario(req):
    return render(req,"mostrarformulario.html")
