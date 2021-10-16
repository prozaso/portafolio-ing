from django.shortcuts import render, redirect
from ..forms import RegistroUsuariosForm, LoginForm
from django.contrib.auth import authenticate, login


def registro_usuarios(request):
    msg = None
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg  = 'Usuario creado.'
            return redirect('login')
        else:
            msg = 'Datos invalidos.'
    else:
        form = RegistroUsuariosForm()
    return render(request,'registration/registro_usuarios.html', {'form': form, 'msg': msg})


def login(request):
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
            msg = 'Error validando el formulario.'
    return render(request, 'login.html', {'form': form, 'msg': msg})
