from django.shortcuts import render
from django.db import connection
import cx_Oracle


def perfil_cliente(request):

    user          = request.user.get_username()
    cliente       = buscar_plan_cliente(user)
    datos_cliente = []
    print(cliente)

    try:
        for x in range(0, 5):
            datos_cliente.append(cliente[0][x])

        for x in range(0, 3):
            datos_cliente.append(cliente[x][5])
    except:
        pass

    data = {
        'cliente' : datos_cliente
    }

    return render(request, 'app/perfil_cliente.html', data)


def buscar_plan_cliente(cli_email):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_BUSCAR_PLAN_CLIENTE", [cli_email, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista