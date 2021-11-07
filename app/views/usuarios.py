from django.shortcuts import render, redirect
from ..forms import RegistroUsuariosForm, LoginForm
from django.contrib.auth import authenticate, login

from django.db import connection
import cx_Oracle


def registro_usuarios(request):
    try:
        msg = None
        if request.method == 'POST':
            #print(request.POST.get('email'))
            #print(request.POST.get('es_cliente'))
            form = RegistroUsuariosForm(request.POST)
            #print(form)
            if form.is_valid():
                user = form.save()
                if request.POST.get('es_cliente'):
                    crear_cliente_servicios(request.POST.get('rut'))
                    
                msg  = 'usuario creado correctamente.'
            else:
                msg = 'datos invalidos.'
        else:
            form = RegistroUsuariosForm()
    except:
        msg = 'datos invalidos.'

    return render(request,'registration/registro_usuarios.html', {'form': form, 'msg': msg})


def login(request):
    try:
        form = LoginForm(request.POST or None)
        msg  = None
        if request.method == 'POST':
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user     = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    msg = 'Credenciales invalidas.'
            else:
                msg = 'Error validando los datos del formulario.'
    except:
        msg = 'Error validando los datos del formulario.'

    return render(request, 'login.html', {'form': form, 'msg': msg})


def crear_cliente_servicios(cliente):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_CREAR_CLIENTE_SERVICIOS', [cliente, salida])

    return salida.getvalue()