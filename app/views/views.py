from django.shortcuts import render
from django.db import connection


# Create your views here.
def home(request):
    
    return render(request, 'app/home.html')


#def lista_regiones():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_REGIONES", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista
