from django.shortcuts import render
from .models import Receta

# Create your views here.
def index(request):
    return render(request, 'index.html')
def contacto (request):
    return render(request, 'contacto.html')
def recetas (request):
    recetas = Receta.objects.all()
    return render(request, 'recetas.html', {'recetas': recetas})
