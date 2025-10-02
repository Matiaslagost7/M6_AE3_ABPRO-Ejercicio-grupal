from django.shortcuts import render
from .models import Receta

# Create your views here.
def index(request):
    recetas = Receta.objects.all()[:3]  # Obtiene las 3 primeras recetas
    return render(request, 'index.html', {'recetas': recetas})

def recetas(request):
    arroz_con_leche = Receta.objects.get(nombre='Arroz con leche')  # Ajusta el nombre si es diferente
    macarrones = Receta.objects.get(nombre='Macarrones')  # Ajusta el nombre si es diferente
    panqueques = Receta.objects.get(nombre='panqueques')  # Ajusta el nombre si es diferente
    return render(request, 'recetas.html', {
        'arroz_con_leche': arroz_con_leche,
        'macarrones': macarrones,
        'panqueques': panqueques
    })

# definimos las acciones del formulario de Contacto
def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        # Aquí se procesan los datos del formulario, como enviarlos por correo o guardarlos en la base de datos
        return render(request, 'contacto.html', {'nombre': nombre})
    return render(request, 'contacto.html')

def arroz_leche(request):
    receta = Receta.objects.get(nombre='Arroz con leche')  # Ajusta el nombre si es diferente
    return render(request, 'arroz-leche.html', {'receta': receta})

def panqueques(request):
    receta = Receta.objects.get(nombre='panqueques')  # Ajusta el nombre si es diferente
    return render(request, 'panqueques.html', {'receta': receta})

def macarrones(request):
    receta = Receta.objects.get(nombre='Macarrones')  # Ajusta el nombre si es diferente
    return render(request, 'macarrones.html', {'receta': receta})
