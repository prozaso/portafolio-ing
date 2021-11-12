from django.shortcuts import redirect, render
from django.db import connection
import cx_Oracle

def capacitaciones(request):

    data = {
        'capacitaciones' : lista_capacitaciones()
    }
    
    if 'buscar'   in request.POST:
        try:
            if request.method == 'POST':
                id      = request.POST.get('cbocap')
                salida  = buscar_capacitacion(id)
                if salida:
                    data['capacitacion'] = salida
                else:
                    data['capacitacion_no_seleccionada'] = 'debes seleccionar una capacitacion antes de buscar!.'
        except:
            data['capacitacion_no_seleccionada'] = 'debes seleccionar una capacitacion antes de buscar!.'

    if 'eliminar' in request.POST:
        try:
            if request.method == 'POST':
                id      = request.POST.get('idcapacitacion')
                salida  = eliminar_capacitacion(id)
                if salida == 1 and id is not None:
                    data['eliminar'] = 'capacitacion eliminada correctamente!.'
                    return redirect('capacitaciones')
                else:
                    data['eliminar'] = 'hubo un error al eliminar la capacitacion.'
        except:
            data['eliminar'] = 'hubo un error al eliminar la capacitacion.'

    if 'agregar'  in request.POST:
        try:
            if request.method == 'POST':
                nombre_servicio = request.POST.get('ncapacitacion')
                salida          = agregar_capacitacion(nombre_servicio)
                if salida == 1:
                    data['agregar'] = 'nueva capacitacion agregada correctamente!.'
                    return redirect('capacitaciones')
                else:
                    data['agregar'] = 'hubo un error al intentar agregar la capacitacion.'
        except:
            data['agregar'] = 'hubo un error al intentar agregar la capacitacion.'

    if 'guardar'  in request.POST:
        try:
            if request.method == 'POST':
                id_capacitacion     = request.POST.get('idcapacitacion')
                nombre_capacitacion = request.POST.get('ncapacitacion')
                salida = modificar_capacitacion(id_capacitacion, nombre_capacitacion)
                if salida == 1 and nombre_capacitacion != '':
                    data['modificar'] = 'cambios realizados correctamente!.'
                    return redirect('capacitaciones')
                else:
                    data['modificar'] = 'hubo un error al intentar guardar los cambios.'
        except:
            data['modificar'] = 'hubo un error al intentar guardar los cambios.'
    
    
    return render(request, 'app/capacitaciones.html', data)


def lista_capacitaciones():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_CAPACITACIONES", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def buscar_capacitacion(capid):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_BUSCAR_CAPACITACION", [capid, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def eliminar_capacitacion(capid):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_CAPACITACION', [capid, salida])

    return salida.getvalue()


def agregar_capacitacion(nombre_cap):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_CAPACITACION', [nombre_cap, salida])

    return salida.getvalue()


def modificar_capacitacion(id_cap, nombre_cap):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_CAPACITACION', [id_cap, nombre_cap, salida])

    return salida.getvalue()
