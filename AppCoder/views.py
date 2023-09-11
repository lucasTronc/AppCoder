from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Cliente, Producto, Envio
from AppCoder.forms import formularioC, formularioE, formularioP


def formularioCliente(request):

    if request.method == 'POST':

        miFormulario = formularioC(request.POST) #aquí mellega toda la información del html

        print(miFormulario)

        if miFormulario.is_valid:   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            cliente = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'], dni=informacion['dni'] ) 

            cliente.save()

            return render(request, "formularioCorrecto.html")

    else: 

        miFormulario= formularioC() #Formulario vacio para construir el html

        return render(request, "formularioCliente.html", {"miFormulario":miFormulario})


def formularioProducto(request):

    if request.method == 'POST':

        miFormulario = formularioP(request.POST) #aquí mellega toda la información del html

        print(miFormulario)

        if miFormulario.is_valid:   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            cliente = Producto(nombre=informacion['nombre'], numero=informacion['numero'], cantidad=informacion['cantidad'] ) 

            cliente.save()

            return render(request, "formularioProducto.html")

    else: 

        miFormulario= formularioP() #Formulario vacio para construir el html

        return render(request, "formularioProducto.html", {"miFormulario":miFormulario})

def formularioEnvio(request):

    if request.method == 'POST':

        miFormulario = formularioE(request.POST) #aquí mellega toda la información del html

        print(miFormulario)

        if miFormulario.is_valid:   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            cliente = Envio(origen=informacion['origen'], destino=informacion['destino'], numero=informacion['numero'], producto=informacion['producto'] ) 

            cliente.save()

            return render(request, "formularioEnvio.html")

    else: 

        miFormulario= formularioE() #Formulario vacio para construir el html

        return render(request, "formularioEnvio.html", {"miFormulario":miFormulario})

def mostrarformulario(request):
    return render(request,"mostrarformulario.html")

def buscar(request:HttpResponse):
    if request.get["nombre"]:
        nombre=request.get["nombre"]
        ficha=Cliente.objects.get(nombre=nombre)
        return render(request," resultadoBusqueda.html", {"nombre":nombre})
    else:
        return HttpResponse(f'agrege un nombre')
