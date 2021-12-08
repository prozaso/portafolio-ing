from django.shortcuts import render
from django.db import connection
import cx_Oracle


def perfil_profesional(request):

    user = request.user.get_username()

    data = {
        'profesional' : datos_profesional(user),
        'clientes'    : profesional_cli_asign(user)
    }

    return render(request, 'app/perfil_profesional.html', data)


def datos_profesional(email_prof):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_BUSCAR_PROF", [email_prof, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def profesional_cli_asign(email_prof):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_PROF_CLI_ASIGN", [email_prof, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista