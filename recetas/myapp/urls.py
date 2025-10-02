from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # aquí se define 'home'
    path('contacto', views.contacto, name='contacto'),
    path ('recetas', views.recetas, name='recetas'),

]
