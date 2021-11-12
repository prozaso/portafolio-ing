from django.shortcuts import render
from django.db import connection
import cx_Oracle

from app.views.capacitaciones import capacitaciones

# Create your views here.
def registro_capacitaciones(request):

    user = request.user.get_username()

    data = {
        'capacitaciones' : lista_capacitaciones(),
        'clientes'       : lista_clientes(),
        'det_cap'        : buscar_detalle_capacitacion_activas(user)
    }

    try:
        if 'guardar':
            if request.method == 'POST':
                capacitacion = request.POST.get('cbocap')
                fecha        = request.POST.get('fecha_cap')
                cliente      = request.POST.get('cbocli')
                salida       = registrar_capacitacion_cliente(capacitacion, fecha, cliente)
                if salida == 1:
                    data['guardar'] = 'registro realizado correctamente!.'
                else:
                    data['guardar'] = 'hubo un error al intentar realizar el registro.'
    except:
            data['guardar'] = 'hubo un error al intentar realizar el registro.'
    

    return render(request, 'app/registro_capacitaciones.html', data)


def lista_capacitaciones():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_CAPACITACIONES", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def lista_clientes():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_CLIENTES", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def registrar_capacitacion_cliente(capacitacion, fecha, cliente):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_REGISTRO_CLIENTE_CAPACITACION', [capacitacion, fecha, cliente, salida])

    return salida.getvalue()


def buscar_detalle_capacitacion(cli_email):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_BUSCAR_DET_CAP", [cli_email, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def buscar_detalle_capacitacion_activas(cli_email):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_BUSCAR_DET_CAP_ACTIVAS", [cli_email, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista