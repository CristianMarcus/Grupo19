from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("aca vamos arrancar a trabajar,exitos compas!")

def saludar(request,nombre):
    return HttpResponse(f"hola {nombre.upper()}")