#from typing_extensions import runtime
from django.shortcuts import redirect, render
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
    
    #####!!!!!!!!!!!!
    if 'agregar_grupo':
            if request.method == 'POST':
                det_cap      = request.POST.get('det_cap_id')
                rut          = request.POST.get('rut')
                nombre       = request.POST.get('nombre')
                registrar_empleado_capacitacion(det_cap, rut, nombre)

                try:
                    for x in range(30):
                        rut      = 'rut'+str(x)
                        nombre   = 'nombre'+str(x)
                        rut_n    = request.POST.get(rut)
                        nombre_n = request.POST.get(nombre)
                        if det_cap != None:
                            registrar_empleado_capacitacion(det_cap, rut_n, nombre_n)
                except:
                    data['grupo'] = 'hubo un error al intentar registrar a los empleados.'

    # FORM ADMIN
    try:
        if 'buscar':
            if request.method == 'POST':
                cliente       = request.POST.get('cbocli')
                salida_buscar = buscar_detalle_capacitacion_activas(cliente)
                if salida_buscar:
                    data['det_caps'] = salida_buscar
                #else:
                    #data['det_caps'] = 'hubo un error al intentar buscar.'

        if 'guardar':
            if request.method == 'POST':
                capacitacion   = request.POST.get('cbocap')
                fecha          = request.POST.get('fecha_cap')
                cliente        = request.POST.get('cbocli')
                salida_guardar = registrar_capacitacion_cliente(capacitacion, fecha, cliente)
                if salida_guardar == 1:
                    data['guardar'] = 'registro realizado correctamente!.'
                    return redirect('registro_capacitaciones')
                #else:
                    #data['guardar'] = 'hubo un error al intentar realizar el registro.'

        if 'lista':
            if request.method == 'POST':
                det_cap_id   = request.POST.get('det_cap_id')
                salida_lista = buscar_listar_empleados(det_cap_id)
                if salida_lista:
                    data['lista'] = salida_lista
                #else:
                    #data['lista'] = 'hubo un error al intentar buscar la lista de empleados.'

    except:
            data['operacion'] = 'hubo un error al intentar realizar la operación.'


    # FORM CLIENTE
    try:
        if 'agregar_grupo':
            if request.method == 'POST':
                det_cap      = request.POST.get('det_cap_id')
                rut          = request.POST.get('rut')
                nombre       = request.POST.get('nombre')
                print(request.POST.get('det_cap_id'))
                print(request.POST.get('rut'))
                print(request.POST.get('nombre'))
                print(user)

                registrar_empleado_capacitacion(det_cap, rut, nombre)

                try:
                    for x in range(30):
                        rut      = 'rut'+str(x)
                        nombre   = 'nombre'+str(x)
                        rut_n    = request.POST.get(rut)
                        nombre_n = request.POST.get(nombre)
                        if det_cap != None:
                            registrar_empleado_capacitacion(det_cap, rut_n, nombre_n)
                except:
                    data['grupo'] = 'hubo un error al intentar registrar a los empleados.'

    except:
            data['operacion'] = 'hubo un error al intentar realizar la operación.'
    

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


def registrar_empleado_capacitacion(det_cap, rut, nombre):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_EMPLEADO_CAPACITACION', [det_cap, rut, nombre, salida])

    return salida.getvalue()


def buscar_listar_empleados(det_emp):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_EMPLEADOS", [det_emp, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista