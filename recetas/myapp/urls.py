from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # aquí se define 'home'
    path('contacto', views.contacto, name='contacto'),
    path ('recetas', views.recetas, name='recetas'),
    path('arroz-leche', views.arroz_leche, name='arroz-leche'),
    path('panqueques', views.panqueques, name='panqueques'),
    path('macarrones', views.macarrones, name='Macarrones'),
    ] 
