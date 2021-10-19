from django.shortcuts import render
from django.db import connection
import cx_Oracle


def contratos(request):

    data = {
        'clientes' : lista_clientes(),
        'rubros'   : lista_rubros(),
        'servicios': lista_servicios()
    }
    #print(lista_clientes())

    if 'buscar' in request.POST:
        if request.method == 'POST':
            cli_email   = request.POST.get('cbocli')
            salida      = buscar_cliente(cli_email)
            if salida:
                data['cliente'] = salida
            else:
                data['cliente_no_seleccionado'] = 'debes seleccionar un cliente antes de buscar!.'
    
    return render(request, 'app/contratos.html', data)


def lista_clientes():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_CLIENTES", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def buscar_cliente(cli_email):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_BUSCAR_CLIENTE", [cli_email, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def lista_rubros():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_RUBROS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def lista_servicios():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_servicios", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista