from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from registros.models import Nombre

# Create your views here.

def Home(request):
    listado = Nombre.objects.all()
    template = loader.get_template('home.html')
    documento = template.render()
    return HttpResponse(documento)


def otra_plantilla(request):
    template = loader.get_template('otra_planilla.html')
    documento = template.render()
    return HttpResponse(documento)