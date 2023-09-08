from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def saludo(req):
    return HttpResponse("hola jordi") 

def saludoConNombre(req,nombre):
    return HttpResponse(f"hola {nombre}") 

def probandoHTML(req):

    plantilla=loader.get_template('template.html')
    documento=plantilla.render()
    return HttpResponse(documento)
