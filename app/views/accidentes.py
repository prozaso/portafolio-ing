from django.shortcuts import render
from django.db import connection
import cx_Oracle

def accidentes(request):

    user = request.user.get_username()

    data = {
        'gravedades' : lista_gravedades(),
        'accidentes' : lista_accidentes(user)
    }

    
    if 'buscar' in request.POST:
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

    if 'ingresar' in request.POST:
        try:
            if request.method == 'POST':
                username = request.user.get_username()
                fecha    = request.POST.get('fecha_acc')
                gravedad = request.POST.get('gravedad')
                detalle  = request.POST.get('detalle_acc')
                salida   = ingresar_accidente(username, fecha, gravedad, detalle)
                if salida == 1:
                    data['ingresar'] = 'accidente ingresado correctamente!.'
                else:
                    data['ingresar'] = 'hubo un error al intentar ingresar los datos.'
        except:
            data['ingresar'] = 'hubo un error al intentar ingresar los datos.'

    if 'guardar' in request.POST:
        try:
            if request.method == 'POST':
                id_rubro     = request.POST.get('idrubro')
                nombre_rubro = request.POST.get('nrubro')
                salida = modificar_rubro(id_rubro, nombre_rubro)
                if salida == 1 and nombre_rubro != '':
                    data['modificar'] = 'cambios realizados correctamente!.'
                else:
                    data['modificar'] = 'hubo un error al intentar guardar los cambios.'
        except:
            data['modificar'] = 'hubo un error al intentar guardar los cambios.'
    
    
    return render(request, 'app/accidentes.html', data)


def lista_accidentes(cliente):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_ACCIDENTES", [cliente, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def lista_gravedades():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_GRAVEDADES", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def buscar_accidente(accid):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_BUSCAR_ACCIDENTE", [accid, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def ingresar_accidente(username, fecha, gravedad, detalle):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_INGRESAR_ACCIDENTE', [username, fecha, gravedad, detalle, salida])

    return salida.getvalue()


def modificar_accidente(id_acc, fecha, alerta, detalle):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_ACCIDENTE', [id_acc, fecha, alerta, detalle, salida])

    return salida.getvalue()
