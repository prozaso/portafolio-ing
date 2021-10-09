from django.conf.urls import url
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('servicios', servicios, name="servicios"),
    path('registro_clientes', registro_clientes, name='registro_clientes'),

]