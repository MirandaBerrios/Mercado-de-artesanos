from django.http import request
from django.shortcuts import render , redirect
from .models import Producto
from .forms import ProductoForm




def AboutUs(request):
    return render(request , "ArtesanosApp/aboutUs.html")

def Contacto_artesanos(request):
    return render(request , "ArtesanosApp/contacto_artesanos.html")

def Home(request):
    return render(request , "ArtesanosApp/home.html")

def Producto_principal(request):
    return render(request , "ArtesanosApp/producto_principal.html")

def Productos(request):
    return render(request , "ArtesanosApp/productos.html")

def Registro_artesanos(request):
    return render(request , "ArtesanosApp/registro_artesanos.html")

