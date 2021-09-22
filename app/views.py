from django.shortcuts import render, redirect
from django.db import connection, models
from .forms import ServicioForm
from .models import Servicio
import cx_Oracle


# Create your views here.
def home(request):
    
    return render(request, 'app/home.html')


def servicios(request):
    
    if 'buscar' in request.POST:
        if request.method == 'POST':
            id = request.POST.get('cboserv')
            #print(id)
    if 'eliminar' in request.POST:
        if request.method == 'POST':
            id = request.POST.get('cboserv')
            salida = eliminar_servicio(id)
            if salida == 1:
                data['eliminar'] = 'Servicio eliminado correctamente'
            else:
                data['eliminar'] = 'Hubo un error al eliminar el servicio'
    
    data = {
        'servicios' : lista_servicios(),
        'servicio'  : servicio_buscar(id)
    }

    print(lista_servicios())

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


def servicio_buscar(servid):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_BUSCAR_SERVICIO", [servid, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def eliminar_servicio(servid):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_SERVICIO', [servid, salida])

    return salida.getvalue()









def lista_regiones():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_REGIONES", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista