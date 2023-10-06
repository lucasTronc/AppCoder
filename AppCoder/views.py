from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
#importacion formularios y modelos (tablas BD)
from AppCoder.models import Cliente, Producto, Envio, Avatar
from AppCoder.forms import formularioC, formularioE, formularioP, AvatarFormulario
#importaciones para login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
#decorador para login
from django.contrib.auth.decorators import login_required
#vistas de clases
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView


def inicio(req):

    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "inicio.html", {"url_avatar": avatar.imagen.url})
    except:
        return render(req, "inicio.html")


def formularioCliente(req):

    if req.method == 'POST':

        miFormulario = formularioC(req.POST) #aquí mellega toda la información del html

        print(miFormulario)

        if miFormulario.is_valid():   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            cliente = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'], dni=informacion['dni'] ) 

            cliente.save()

            clientes=Cliente.objects.all() 

            return render(req,"listarClientes.html",{"clientes":clientes})
    else: 

        miFormulario= formularioC() #Formulario vacio para construir el html

        return render(req, "formularioCliente.html", {"miFormulario":miFormulario})


def formularioProducto(req):

    if req.method == 'POST':

        miFormulario = formularioP(req.POST) #aquí mellega toda la información del html

        print(miFormulario)

        if miFormulario.is_valid():   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            producto = Producto(nombre=informacion['nombre'], numero=informacion['numero'], cantidad=informacion['cantidad'] ) 

            producto.save()

            productos=Producto.objects.all() 

            return render(req,"listarProductos.html",{"productos":productos})

    else: 

        miFormulario= formularioP() #Formulario vacio para construir el html

        return render(req, "formularioProducto.html", {"miFormulario":miFormulario})


def formularioEnvio(req):

    if req.method == 'POST':

        miFormulario = formularioE(req.POST) #aquí mellega toda la información del html

        print(miFormulario)

        if miFormulario.is_valid():   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            envio = Envio(origen=informacion['origen'], destino=informacion['destino'], numero=informacion['numero'], producto=informacion['producto']) 

            envio.save()

            envios=Envio.objects.all() 

            return render(req,"listarEnvios.html",{"envios":envios})


    else: 

        miFormulario= formularioE() #Formulario vacio para construir el html

        return render(req, "formularioEnvio.html", {"miFormulario": miFormulario})


def contactTermPrivacy(req:HttpResponse):
        return render(req,"contactTermPrivacy.html")


def mostrarformulario(req):
    return render(req,"mostrarformulario.html")


def buscar(req:HttpResponse):
    nombre=req.GET.get("nombre")
    if nombre:
        ficha=Cliente.objects.filter(nombre__icontains=nombre)
        return render(req,"resultadoBusqueda.html", {"ficha":ficha})
    else:
        return render(req,"resultadoErroneo.html")


def about(req:HttpResponse):
        return render(req,"about.html")


def loginView(req):

    if req.method == 'POST':

        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)
            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje": f"Bienvenido {usuario}!"})
            
        return render(req, "inicio.html", {"mensaje": f"Datos incorrectos"})
    else:
        miFormulario = AuthenticationForm()
        return render(req, "login.html", {"miFormulario": miFormulario})


def register(req):

    if req.method == 'POST':

        miFormulario = UserCreationForm(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]
            miFormulario.save()
            return render(req, "inicio.html", {"mensaje": f"Usuario {usuario} creado con éxito!"})

        return render(req, "inicio.html", {"mensaje": f"Formulario invalido"})
            
    else:
        miFormulario = UserCreationForm()
        return render(req, "registro.html", {"miFormulario": miFormulario})

@login_required
def editarPerfil(req):

    usuario = req.user
    if req.method == 'POST':

        miFormulario = UserChangeForm(req.POST, instance=req.user)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()

            return render(req, "inicio.html", {"mensaje": "Datos actualizados con éxito!"})
        else:
            return render(req, "editarPerfil.html", {"miFormulario": miFormulario})

    else:
        miFormulario = UserChangeForm(instance=usuario)
        return render(req, "editarPerfil.html", {"miFormulario": miFormulario})

@login_required
def agregarAvatar(req):

    if req.method == 'POST':

        miFormulario = AvatarFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data

            avatar = Avatar(user=req.user, imagen=data["imagen"])

            avatar.save()

            return render(req, "inicio.html", {"mensaje": "Avatar actualizados con éxito!"})

    else:
        miFormulario = AvatarFormulario()
        return render(req, "agregarAvatar.html", {"miFormulario": miFormulario})
    

class ListarClientes(ListView):
    model = Cliente
    template_name = "listarClientes.html"
    context_object_name = "clientes"


class DetalleClientes(DetailView):
    model = Cliente
    template_name = "detalleClientes.html"
    context_object_name = "clientes"


class ListarProductos(ListView):
    model = Producto
    template_name = "listarProductos.html"
    context_object_name = "productos"


class DetalleProductos(DetailView):
    model = Producto
    template_name = "detalleProductos.html"
    context_object_name = "productos"


class ListarEnvios(ListView):
    model = Envio
    template_name = "listarEnvios.html"
    context_object_name = "envios"


class DetalleEnvios(DetailView):
    model = Envio
    template_name = "detalleEnvios.html"
    context_object_name = "envios"