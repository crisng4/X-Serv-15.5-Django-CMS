
from django.shortcuts import render
from models import Pages
from django.http import HttpResponse, HttpResponseNotFound

 # Create your views here.

def nueva(request,name):
    try:
        pagina = Pages.objects.get(name = name)
        return HttpResponse(pagina.page)
    except Pages.DoesNotExist:
        return HttpResponse("<h3> Pagina no encontrada, " + name + "</h3>")

def guardar(request,name,url):
    pagina = Pages(name = name,page = url)
    pagina.save()
    return HttpResponse(" Pagina guardada: "+name)

def mostrar(request):
    respuesta = ""
    lista_pags = Pages.objects.all()
    for pag in lista_pags:
        respuesta+="<li>"+ pag.name + " : " + pag.page + "</li>"
    return HttpResponse(respuesta)

def Error404(request,cont1,cont2):
    return HttpResponse (" Error404 Not Found")
