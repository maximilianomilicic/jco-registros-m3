from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

# Create your views here.

def Home(request):
    doc_externo = open("E:/Programacion-proyectos/jco-registros-m3/registrosdem3/registros/template/home.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def otra_plantilla(request):
    template = loader.get_template('otra_planilla.html')
    documento = template.render()
    return HttpResponse(documento)