from django import forms
from .models import Servicio
from django.forms import ModelForm

class ServicioForm(ModelForm):

    class Meta:
        model = Servicio
        fields = ['nombre_serv', 'valor_serv']