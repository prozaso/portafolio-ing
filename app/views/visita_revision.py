from django.shortcuts import render
from django.db import connection
import cx_Oracle

# Create your views here.
def visita_revision(request):

    user = request.user.get_username()
    #print(visitas_activas(user))

    data = {
        'clientes' : lista_clientes(),
        'visitas'  : visitas_activas(user)
    }

    if 'guardar'  in request.POST:
        try:
            if request.method == 'POST':
                cliente     = request.POST.get('cbocli')
                fecha       = request.POST.get('fecha_visita')
                salida      = asignar_visita(fecha, cliente)
                if salida == 1:
                    data['visita'] = 'visita agendada correctamente!.'
                else:
                    data['visita'] = 'hubo un error al intentar asignar visita.'
        except:
            data['visita'] = 'hubo un error al intentar asignar visita.'
    
    if 'guardar_datos_visita'  in request.POST:
        try:
            if request.method == 'POST':
                codigo     = request.POST.get('det_vis_id')
                datos      = request.POST.get('datos_visita')
                salida     = guardar_datos_visita(codigo, datos)
                if salida == 1:
                    data['guardar_datos'] = 'datos guardados correctamente!.'
                else:
                    data['guardar_datos'] = 'hubo un error al intentar ingresar los datos.'
        except:
            data['guardar_datos'] = 'hubo un error al intentar ingresar los datos.'


    return render(request, 'app/visita_revision.html', data)


def lista_clientes():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_CLIENTES", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def asignar_visita(fecha, cliente):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ASIGNAR_VISITA', [fecha, cliente, salida])

    return salida.getvalue()


def visitas_activas(profesional):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_BUSCAR_VIS_ACTIVAS", [profesional, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def guardar_datos_visita(codigo, datos):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_GUARDAR_DAT_VIS', [codigo, datos, salida])

    return salida.getvalue()