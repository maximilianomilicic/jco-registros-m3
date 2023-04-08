from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

# Create your views here.

def Home(request):
    template = loader.get_template('home.html')
    documento = template.render()
    return HttpResponse(documento)


def otra_plantilla(request):
    template = loader.get_template('otra_planilla.html')
    documento = template.render()
    return HttpResponse(documento)