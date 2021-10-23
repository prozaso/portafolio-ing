from django import forms
from .models import Servicio, User
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm

class ServicioForm(ModelForm):

    class Meta:
        model  = Servicio
        fields = ['nombre_serv', 'valor_serv']

##################################################################################################################

class LoginForm(forms.Form):
    
    class Meta:
        model  = User
        fields = ['username', 'password']


class RegistroUsuariosForm(UserCreationForm):
    
    class Meta:
        model  = User
        fields = ('email', 'password1', 'password2', 'es_cliente', 'es_profesional', 
                  'es_administrador', 'razon_social', 'rut', 'telefono', 'direccion',
                  'first_name', 'last_name')