from django.shortcuts import redirect, render
from django.db import connection
import cx_Oracle

def rubros(request):

    data = {
        'rubros' : lista_rubros()
    }
    
    if 'buscar'   in request.POST:
        try:
            if request.method == 'POST':
                id      = request.POST.get('cborub')
                salida  = buscar_rubro(id)
                if salida:
                    data['rubro'] = salida
                else:
                    data['rubro_no_seleccionado'] = 'debes seleccionar un rubro antes de buscar!.'
        except:
            data['rubro_no_seleccionado'] = 'debes seleccionar un rubro antes de buscar!.'

    if 'eliminar' in request.POST:
        try:
            if request.method == 'POST':
                id      = request.POST.get('idrubro')
                salida  = eliminar_rubro(id)
                if salida == 1 and id is not None:
                    data['eliminar'] = 'rubro eliminado correctamente!.'
                    return redirect('rubros')
                else:
                    data['eliminar'] = 'hubo un error al eliminar el rubro.'
        except:
            data['eliminar'] = 'hubo un error al eliminar el rubro.'

    if 'agregar'  in request.POST:
        try:
            if request.method == 'POST':
                nombre_rubro = request.POST.get('nrubro')
                salida       = agregar_rubro(nombre_rubro)
                if salida == 1:
                    data['agregar'] = 'nuevo rubro agregado correctamente!.'
                    return redirect('rubros')
                else:
                    data['agregar'] = 'hubo un error al intentar agregar el rubro.'
        except:
            data['agregar'] = 'hubo un error al intentar agregar el rubro.'

    if 'guardar'  in request.POST:
        try:
            if request.method == 'POST':
                id_rubro     = request.POST.get('idrubro')
                nombre_rubro = request.POST.get('nrubro')
                salida       = modificar_rubro(id_rubro, nombre_rubro)
                if salida == 1 and nombre_rubro != '':
                    data['modificar'] = 'cambios realizados correctamente!.'
                    return redirect('rubros')
                else:
                    data['modificar'] = 'hubo un error al intentar guardar los cambios.'
        except:
            data['modificar'] = 'hubo un error al intentar guardar los cambios.'
    
    
    return render(request, 'app/rubros.html', data)


def lista_rubros():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_RUBROS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def buscar_rubro(rubid):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_BUSCAR_RUBRO", [rubid, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def eliminar_rubro(rubid):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_RUBRO', [rubid, salida])

    return salida.getvalue()


def agregar_rubro(nombre_rub):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_RUBRO', [nombre_rub, salida])

    return salida.getvalue()


def modificar_rubro(id_rub, nombre_rub):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_RUBRO', [id_rub, nombre_rub, salida])

    return salida.getvalue()
