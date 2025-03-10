from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def saludar(request):
    return HttpResponse("Hola desde Django!")

def saludar_con_etiqueta(request):
    return HttpResponse('<h1>Hola desde Django con etiquetas!</h1>')

def saludar_con_parametros(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"Hola {nombre} {apellido} desde Django con parametros!")

def index(request):
    from datetime import datetime
    año_actual = datetime.now().year
    contexto = {"año": año_actual}
    #print(año_actual)
    return render(request, "core/index.html", contexto)