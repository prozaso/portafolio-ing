from django.shortcuts import render, redirect
from django.db import connection, models
from .forms import ServicioForm
from .models import Servicio
import cx_Oracle


# Create your views here.
def home(request):
    
    return render(request, 'app/home.html')


def servicios(request):
    data = {
        'servicios': lista_servicios()
    }
    print(servicios)
    return render(request, 'app/servicios.html', data)


def lista_servicios():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_servicios", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def lista_regiones():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_REGIONES", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista