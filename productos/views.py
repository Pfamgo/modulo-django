from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto


# Create your views here.
def index(request):
    #VE A BUSCAR LOS PRODUCTOS A LA BASE DE DATOS Y PASASELOS AL HTML
    productos = Producto.objects.all()
    return render(request, 'productos/home.html', {'productos':productos})

def dashboard(request):
    return HttpResponse("dashboard")

def login(request):
    return HttpResponse("login")

def register(request):
    return HttpResponse("register")

def venta(request):
    return HttpResponse("venta")





