from django.shortcuts import render
from django.db import Error
from appPeliculas.models import Generos, Peliculas
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def vistaGenero(request):
    return render(request, "agregarGenero.html")

@csrf_exempt
def agregarGenero(request):
    try:
        newNombre = request.POST['txtNombre']
        genero=Generos(nombre=newNombre)
        
        genero.save()
        mensaje = "Género Agragado correctamente"
    except Error as error:
        mensaje =str(error)
    retorno = {"mensaje":mensaje}
    return render(request, "agregarGenero.html", retorno)

def listarPeliculas(request):
    peliculas = Peliculas.objects.all().values()
    print(peliculas)
    retorno = {"peliculas": list(peliculas)}
    return JsonResponse(retorno, content_type='application/json')

