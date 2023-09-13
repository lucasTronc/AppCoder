from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Cliente, Producto, Envio
from AppCoder.forms import formularioC, formularioE, formularioP


def formularioCliente(req):

    if req.method == 'POST':

        miFormulario = formularioC(req.POST) #aquí mellega toda la información del html

        print(miFormulario)

        if miFormulario.is_valid():   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            cliente = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'], dni=informacion['dni'] ) 

            cliente.save()

            return render(req, "formularioCorrecto.html")

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

            return render(req,"formularioCorrecto.html")

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

            #return render(req, "formularioCorrecto.html")
            return render(req, "formularioEnvio.html", {"miFormulario": miFormulario})

    else: 

        miFormulario= formularioE() #Formulario vacio para construir el html

        return render(req, "formularioEnvio.html", {"miFormulario": miFormulario})

def mostrarformulario(req):
    return render(req,"mostrarformulario.html")

def buscar(req:HttpResponse):

    nombre=req.GET.get("nombre")
    if nombre:
        ficha=Cliente.objects.filter(nombre__icontains=nombre)
        return render(req," resultadoBusqueda.html", {"ficha":ficha})
    else:
        return HttpResponse(f'agrege un nombre')
