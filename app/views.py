from django.shortcuts import render, redirect
from django.db import connection, models
from .forms import ServicioForm, SignUpForm, LoginForm
from .models import Servicio
import cx_Oracle


from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    
    return render(request, 'app/home.html')


def servicios(request):

    data = {
        'servicios' : lista_servicios()
    }
    #print(servicios)
    
    if 'buscar' in request.POST:
        if request.method == 'POST':
            id      = request.POST.get('cboserv')
            salida  = servicio_buscar(id)
            if salida:
                data['servicio'] = salida
            else:
                data['servicio_no_seleccionado'] = 'debes seleccionar un servicio antes de buscar!.'

    if 'eliminar' in request.POST:
        if request.method == 'POST':
            id      = request.POST.get('idservicio')
            salida  = eliminar_servicio(id)
            if salida == 1 and id is not None:
                data['eliminar'] = 'servicio eliminado correctamente!.'
            else:
                data['eliminar'] = 'hubo un error al eliminar el servicio.'

    if 'agregar' in request.POST:
        if request.method == 'POST':
            nombre_servicio = request.POST.get('nservicio')
            valor_servicio  = request.POST.get('vservicio')
            salida = agregar_servicio(nombre_servicio, valor_servicio)
            if salida == 1:
                data['agregar'] = 'nuevo servicio agregado correctamente!.'
            else:
                data['agregar'] = 'hubo un error al intentar agregar el servicio.'

    if 'guardar' in request.POST:
        if request.method == 'POST':
            id_servicio     = request.POST.get('idservicio')
            nombre_servicio = request.POST.get('nservicio')
            valor_servicio  = request.POST.get('vservicio')
            salida = modificar_servicio(id_servicio, nombre_servicio, valor_servicio)
            if salida == 1 and nombre_servicio != '':
                data['modificar'] = 'cambios realizados correctamente!.'
            else:
                data['modificar'] = 'hubo un error al intentar guardar los cambios.'
    
    
    return render(request, 'app/servicios.html', data)


def lista_servicios():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_servicios", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def servicio_buscar(servid):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_BUSCAR_SERVICIO", [servid, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def eliminar_servicio(servid):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_SERVICIO', [servid, salida])

    return salida.getvalue()


def agregar_servicio(nombre_serv, valor_serv):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_SERVICIO', [nombre_serv, valor_serv, salida])

    return salida.getvalue()


def modificar_servicio(id_serv, nombre_serv, valor_serv):

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_SERVICIO', [id_serv, nombre_serv, valor_serv, salida])

    return salida.getvalue()


#def lista_regiones():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_REGIONES", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


##################################################################################################################

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('/')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'registration/register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})
