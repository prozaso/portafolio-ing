from django.shortcuts import render
from django.db import connection
import cx_Oracle


def pagos(request):

    user = request.user.get_username()

    data = {
        'tipos_pago' : lista_tipo_pago(),
        'pago'       : listar_pago(user)
    }

    if 'pagar' in request.POST:
        if request.method == 'POST':
            tipo   = request.POST.get('cbotipo')
            valor  = request.POST.get('valor')
            salida = agregar_pago(tipo, user, valor.strip())
            if salida == 1:
                data['intento_pago'] = 'el pago fue realizado correctamente!.'
            else:
                data['intento_pago'] = 'hubo un error al intentar realizar el pago.'


    return render(request, 'app/pagos.html', data)


def lista_tipo_pago():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_TIPO_PAGO", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def agregar_pago(tipo, cliente, valor):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_PAGO', [tipo, cliente, valor, salida])

    return salida.getvalue()


def listar_pago(cliente):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PAGO", [cliente, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista