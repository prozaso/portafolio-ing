from django.shortcuts import render
from django.db import connection
import cx_Oracle


def lista_visitas(request):

    user = request.user.get_username()

    data = {
        'visitas_cli' : visitas_cliente(user),
        'visitas_pro' : visitas_profesional(user),
        'visitas_adm' : visitas_administrador()
    }

    return render(request, 'app/lista_visitas.html', data)


def visitas_cliente(cliente):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_VISITAS_CLI", [cliente, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def visitas_profesional(profesional):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_VISITAS_PRO", [profesional, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def visitas_administrador():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_VISITAS_ADM", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista