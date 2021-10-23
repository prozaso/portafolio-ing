#from typing_extensions import runtime
from django.shortcuts import render
from django.db import connection
import cx_Oracle


def contratos(request):

    data = {
        'clientes'      : lista_clientes(),
        'rubros'        : lista_rubros(),
        'servicios'     : lista_servicios(),
        'regiones'      : lista_regiones(),
        'profesionales' : lista_profesionales()
    }

    if 'buscar' in request.POST:
        try:
            if request.method == 'POST':
                cli_email   = request.POST.get('cbocli')
                salida      = buscar_cliente(cli_email)
                if salida:
                    data['cliente'] = salida
                else:
                    data['cliente_no_seleccionado'] = 'debes seleccionar un cliente antes de buscar!.'
        except:
            data['cliente_no_seleccionado'] = 'debes seleccionar un cliente antes de buscar!.'

    if 'buscaremail' in request.POST:
        try:
            if request.method == 'POST':
                cli_email   = request.POST.get('bemail')
                salida      = buscar_cliente(cli_email)
                if salida:
                    data['cliente'] = salida
                else:
                    data['cliente_no_seleccionado'] = 'debes ingresar un correo valido antes de buscar!.'
        except:
            data['cliente_no_seleccionado'] = 'debes ingresar un correo valido antes de buscar!.'

    if 'crearcontrato' in request.POST:
        try:
            if request.method == 'POST':
                #username    = request.user.get_username()
                cliente      = request.POST.get('rutempresa')
                rubro       = request.POST.get('cborub')
                servicio    = request.POST.get('cboserv')
                comuna      = request.POST.get('comuna')
                profesional = request.POST.get('profesional')
            
                salida      = crear_contrato(rubro, servicio, comuna, cliente, profesional)
                if salida == 1:
                    data['mensaje_contrato'] = 'contrato creado correctamente!.'
                else:
                    data['mensaje_contrato'] = 'hubo un error al intentar crear el contrato, por favor verifique los datos.'
        except:
            data['mensaje_contrato'] = 'hubo un error al intentar crear el contrato, por favor verifique los datos.'


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


def lista_profesionales():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PROFESIONALES", [out_cur])

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


def lista_regiones():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_REGIONES", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def lista_comunas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_COMUNAS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def lista_comunas_por_region(regid):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_COMUNAS_POR_REGION", [out_cur, regid])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def select_comuna_por_region(request):
    # En la url del script en el template
    # debe ir el nombre de la variable que usaremos
    # tal cual la usamos acá para traerla
    # y como se llama en el select de donde la obtenemos
    # como en las dos siguientes lineas de codigo:

    #let url = '/comunas/?region='+regionId;
    reg = request.GET.get('region')
    data = {
        'comunas':lista_comunas_por_region(reg)
    }
    
    return render(request, 'app/select_comunas.html', data)


def crear_contrato(rubro, servicio, comuna, cliente, profesional):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_CREAR_CONTRATO', [rubro, servicio, comuna, cliente, profesional, salida])

    return salida.getvalue()